from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from contextlib import asynccontextmanager
import torch
from src.textSummarizerWebApplication.entity import ModelApiEntity


class ModelApiCreating:

    def __init__(self, config: ModelApiEntity):
        self.config = config

    def main(self):
        
        @asynccontextmanager
        async def lifespan(app: FastAPI):
            app.state.tokenizer = AutoTokenizer.from_pretrained("sametmete3436/t5-small-summarizer")
            app.state.model = AutoModelForSeq2SeqLM.from_pretrained("sametmete3436/t5-small-summarizer")
            app.state.model.eval()
            yield

        app = FastAPI(lifespan=lifespan)

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_methods=["*"],
            allow_headers=["*"],
        )

        class TextRequest(BaseModel):
            text: str

        @app.post("/summarize")
        async def summarize_text(request_body: TextRequest, request: Request):
            model = request.app.state.model
            tokenizer = request.app.state.tokenizer
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)

            inputs = tokenizer(
                request_body.text,
                return_tensors="pt",
                truncation=True,
                max_length=512
            )
            inputs = {k: v.to(device) for k, v in inputs.items()}

            with torch.no_grad():
                summary_ids = model.generate(
                    input_ids=inputs["input_ids"],
                    attention_mask=inputs["attention_mask"],
                    max_length=128,
                    num_beams=4
                )

            summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            return {"summary": summary}

        return app