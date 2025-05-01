from models import User
from schemas import UserCreate, UserLogin, UserOut
from fastapi import APIRouter, HTTPException, status
import auth
import json

router = APIRouter()

@router.get("/health", response_model=dict, status_code=status.HTTP_200_OK)
async def health_check() -> dict:
    return {
        "success": True,
        "message": "API is healthy",
        "status": "OK"
    }

@router.post("/register",response_model=dict, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate) -> User:
    existing_user = await User.get_or_none(email=user.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    new_user = await User.create(
        username=user.username,
        email=user.email,
        hashed_password=auth.hash_password(user.password),
        full_name=user.full_name,
        phone_number=user.phone_number,
        address=user.address,
        language=user.language,
        utm_source=user.utm_source,
        device_used=user.device_used,
        location=user.location
    )
    return {
        "success": True,
        "message": "User created successfully",
        "user": new_user.dict()
    }

@router.post("/login", response_model=dict, status_code=status.HTTP_200_OK)
async def login_user(user_login: UserLogin) -> str:
    user = await User.get_or_none(email=user_login.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials"
        )
    if not auth.verify_password(user_login.password, user.hashed_password):
        raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
        )
    return {
        "success": True,
        "message": "Login successful",
        "token_type": "Bearer",
        "token": auth.get_token_jwt(user),
    }
    
    
