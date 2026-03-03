from fastapi import FastAPI, HTTPException,Request
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel
import torch
from src.textSummarizerWebApplication.entity import ModelApiEntity


class ModelApiCreating:

    def __init__(self, config:ModelApiEntity):
        self.config = config
    app = FastAPI()

    class TextRequest(BaseModel):
        text: str

        @classmethod
        def validate(cls, value):
            if not isinstance(value.text, str):
                raise ValueError("text must be a string")
            return value

    def get_ModelPkl(self):
        with open(self.config.model_path, "rb") as f:
            model = pickle.load(f)
        return model
    def get_TokenizerPkl(self):
        with open(self.config.tokenizer_path, "rb") as f:
            tokenizer = pickle.load(f)
        return tokenizer
    
    def create_app(self):
        """Load model/tokenizer and attach to app state, return ready-to-run app."""
        model = self.get_ModelPkl()
        tokenizer = self.get_TokenizerPkl()
        # attach to the FastAPI app state so endpoints can access them
        self.app.state.model = model
        self.app.state.tokenizer = tokenizer
        return self.app

    @app.post("/summarize")
    async def summarize_text(request_body: TextRequest, request: Request):
        """Endpoint that receives validated text and returns a generated summary.

        The model and tokenizer are not parameters to this function; they are
        loaded once during app startup and stored on ``app.state`` by the
        pipeline or entrypoint.
        """
    # retrieve the pre-loaded objects from the application state
        model = request.app.state.model
        tokenizer = request.app.state.tokenizer


        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model.to(device)
        model.eval()
        # input is already validated by Pydantic; ensure text is string
        text = request_body.text
        # ... perform summarization using self.model or other logic
        inputs = tokenizer(
            text,
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

