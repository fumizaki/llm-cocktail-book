from fastapi import FastAPI
from src.presentation.controller import (
    rag,
    chatbot
)


app = FastAPI()


app.include_router(
    rag.router
)

app.include_router(
    chatbot.router
)
