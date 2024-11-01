from fastapi import APIRouter
from src.application.usecase.rag.generation import GenerationUsecase
from src.application.usecase.rag.indexing import IndexingUsecase


router = APIRouter()

@router.post("/indexing/text")
async def indexing_text(prompt: str):
    usecase = IndexingUsecase()
    await usecase.prompt_indexing_exec(prompt)
    return None


@router.get("/generation/txt2txt")
async def generation_txt2txt(query: str):
    usecase = GenerationUsecase()
    result = await usecase.txt2txt_exec(query)
    return {"response": result}