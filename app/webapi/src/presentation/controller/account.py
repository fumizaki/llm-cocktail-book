from fastapi import APIRouter, status, HTTPException, Depends

router = APIRouter()

@router.get("/account/profile")
async def get_account_profile():
    return 


@router.put("/account/password")
async def update_account_password():
    return