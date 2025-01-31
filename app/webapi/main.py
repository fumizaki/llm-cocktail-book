from fastapi import FastAPI
from src.presentation.controller import (
    oauth,
    chatbot,
    credit,
    webhook
)


app = FastAPI()


app.include_router(
    oauth.router
)

app.include_router(
    chatbot.router
)

app.include_router(
    credit.router
)
app.include_router(
    webhook.router
)


