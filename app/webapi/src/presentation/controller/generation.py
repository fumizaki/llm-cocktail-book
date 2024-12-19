from fastapi import APIRouter, Depends
from src.presentation.dependency.usecase.generation import implement_generation_code_usecase
from src.application.generation.code import CodeGenerationUsecase, Txt2CodeModel


router = APIRouter()

@router.post("/generation/txt2code")
async def txt2code(form: Txt2CodeModel, usecase: CodeGenerationUsecase = Depends(implement_generation_code_usecase)):
    result = await usecase.txt2code_exec(form)
    return result


