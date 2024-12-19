from fastapi import Depends
from src.application.generation.code import CodeGenerationUsecase
from src.domain.entity.credential import Credential
from src.presentation.dependency.authorization import get_credential_from_header


def implement_generation_code_usecase(
        credential: Credential = Depends(get_credential_from_header),
    ):
    return CodeGenerationUsecase(
        credential
        )