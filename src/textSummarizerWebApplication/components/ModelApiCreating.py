from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from contextlib import asynccontextmanager
import httpx
import os
from src.textSummarizerWebApplication.entity import ModelApiEntity


class ModelApiCreating:

    def __init__(self, config: ModelApiEntity):
        self.config = config

    def main(self):

        @asynccontextmanager
        async def lifespan(app: FastAPI):
            app.state.client = httpx.AsyncClient(timeout=60.0)
            yield
            await app.state.client.aclose()

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
            hf_token = os.getenv("HF_TOKEN")
            client = request.app.state.client

            response = await client.post(
                "https://router.huggingface.co/models/sametmete3436/t5-small-summarizer",
                headers={"Authorization": f"Bearer {hf_token}"},
                json={"inputs": request_body.text}
            )

            if response.status_code != 200:
                raise HTTPException(status_code=response.status_code, detail=response.text)

            return {"summary": response.json()[0]["summary_text"]}

        return app