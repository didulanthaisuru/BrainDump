from fastapi import APIRouter, HTTPException
from schemas.user_signup import SignupRequest, SignupResponse
from services.user_signup import signup as signup_service

router = APIRouter(prefix="/signup", tags=["signup"])

@router.post("/signup", response_model=SignupResponse)
async def signup_endpoint(user_data: SignupRequest):
    user = await signup_service(user_data)
    return user
