from fastapi import APIRouter
from src.application.rag.indexing.usecase import RagIndexingUsecase


router = APIRouter()

@router.post("/indexing/text")
async def indexing_text(prompt: str):
    usecase = RagIndexingUsecase()
    await usecase.prompt_indexing_exec(prompt)
    return None

