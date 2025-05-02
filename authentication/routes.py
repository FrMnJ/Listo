from interservice_communication import assign_role
from models import User
from schemas import UserCreate, UserLogin, UserOut, VerifyToken
from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
import auth

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
    if not await assign_role(new_user.id, "user"):
        await new_user.delete()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to assign role"
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
    response = JSONResponse(
        content= {
        "success": True,
        "message": "Login successful",
        "token_type": "Bearer",
        "access_token": auth.get_access_token_jwt(user),
        "refresh_token": auth.get_refresh_token_jwt(user),
    })
    response.set_cookie(
        key="refresh_token",
        value=auth.get_refresh_token_jwt(user),
        httponly=True,
        secure=True,
        max_age=60*60*24*7,
    )
    return response

@router.post("/verify-token", response_model=dict, status_code=status.HTTP_200_OK) 
async def verify_token(verify_token: VerifyToken) -> dict:
    try:
        payload = auth.verify_token_jwt(verify_token.token)
        print(not payload)
        if not payload:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token"
            )
        return {
            "isValid": True,
            "user": payload
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        ) from e
    
@router.post("/refresh", response_model=dict, status_code=status.HTTP_200_OK)
async def refresh_token(refresh_token: str) -> dict:
    payload = auth.verify_token_jwt(refresh_token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )
    user = await User.get_or_none(id=payload["user_id"])
    if not user:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Invalid token"
        )
    new_access_token = auth.get_access_token_jwt(user)
    response = JSONResponse(
        content={
            "success": True,
            "message": "Token refreshed successfully",
            "token_type": "Bearer",
            "token": new_access_token,
        }
    )
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        secure=True,
        max_age=60*60*24*7,
    )
    return response

@router.get("/logout", response_model=dict, status_code=status.HTTP_200_OK)
async def logout_user() -> dict:
    response = JSONResponse(
        content={
            "success": True,
            "message": "Logout successful",
        }
    )
    response.delete_cookie("refresh_token")
    return response

    
