from fastapi import APIRouter, status, HTTPException, Depends
from fastapi.responses import RedirectResponse
from src.presentation.dependency.usecase.oauth import (
    implement_oauth_signup_usecase,
    implement_oauth_password_usecase,
    implement_oauth_refresh_usecase
)
from src.application.oauth import (
    OAuthSignupUsecase,
    OAuthSignupModel,
    OAuthPasswordUsecase,
    OAuthPasswordModel,
    OAuthRefreshUsecase,
    OAuthRefreshModel
)


router = APIRouter()

@router.post("/oauth/signup")
async def oauth_signup(form: OAuthSignupModel, usecase: OAuthSignupUsecase = Depends(implement_oauth_signup_usecase)):
    result = usecase.request_exec(form)
    return result

@router.get("/oauth/signup/verify")
async def oauth_verify(key: str, usecase: OAuthSignupUsecase = Depends(implement_oauth_signup_usecase)):
    result = usecase.verify_exec(key)
    return result


@router.post("/oauth/signin")
async def oauth_signin(form: OAuthPasswordModel, usecase: OAuthPasswordUsecase = Depends(implement_oauth_password_usecase)):
    result = usecase.token_exec(form)
    return result


@router.post("/oauth/refresh")
async def oauth_refresh(form: OAuthRefreshModel, usecase: OAuthRefreshUsecase = Depends(implement_oauth_refresh_usecase)):
    result = usecase.token_exec(form)
    return result