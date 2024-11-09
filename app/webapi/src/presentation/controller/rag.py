from fastapi import APIRouter
from src.application.usecase.rag.generation import RagGenerationUsecase
from src.application.usecase.rag.indexing import RagIndexingUsecase


router = APIRouter()

@router.post("/indexing/text")
async def indexing_text(prompt: str):
    usecase = RagIndexingUsecase()
    await usecase.prompt_indexing_exec(prompt)
    return None


@router.get("/generation/txt2txt")
async def generation_txt2txt(query: str):
    usecase = RagGenerationUsecase()
    result = await usecase.txt2txt_exec(query)
    return {"response": result}