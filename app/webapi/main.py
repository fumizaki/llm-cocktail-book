from fastapi import FastAPI
from src.presentation.controller import (
    oauth,
    chatbot,
    rag,
)


app = FastAPI()


app.include_router(
    oauth.router
)

app.include_router(
    chatbot.router
)

app.include_router(
    rag.router
)
