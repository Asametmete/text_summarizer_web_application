from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pickle
from pydantic import BaseModel
import torch
from src.textSummarizerWebApplication.entity import ModelApiEntity

class ModelApiCreating:

    def __init__(self, config: ModelApiEntity):
        self.config = config
        self.app = FastAPI()
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"]
        )
        self.model = self.get_ModelPkl()
        self.tokenizer = self.get_TokenizerPkl()

    def create_app(self):
        @self.app.post("/summarize")
        async def summarize_text(request: ModelApiCreating.TextRequest):
                return await self._summarize(request)
    
        return self.app

    class TextRequest(BaseModel):
        text: str

    def get_ModelPkl(self):
        with open(self.config.model_path, "rb") as f:
            model = pickle.load(f)
        return model

    def get_TokenizerPkl(self):
        with open(self.config.tokenizer_path, "rb") as f:
            tokenizer = pickle.load(f)
        return tokenizer

    async def _summarize(self, request: 'ModelApiCreating.TextRequest'):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(device)
        self.model.eval()

        inputs = self.tokenizer(
            request.text,
            return_tensors="pt",
            truncation=True,
            max_length=512
        )
        inputs = {k: v.to(device) for k, v in inputs.items()}

        with torch.no_grad():
            summary_ids = self.model.generate(
                input_ids=inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                max_length=128,
                num_beams=4
            )

        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return {"summary": summary}

