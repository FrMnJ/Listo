import os
from passlib.context import CryptContext
from models import User
import jwt
from datetime import datetime, timedelta
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hash a password using Bcrypt.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verify a password against a hashed password.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_token_jwt(user: User, expires_delta: Optional[timedelta] = None) -> str:
    """
    Generate a JWT token for the user.
    """
    data = {
        "email": user.email,
        "username": user.username,
        "full_name": user.full_name,
        "phone_number": user.phone_number,
        "address": user.address,
        "language": user.language,
        "utm_source": user.utm_source,
        "device_used": user.device_used,
        "location": user.location,
        "exp": datetime.now(datetime.timezone.utc) + (expires_delta or timedelta(minutes=15)), 
        "iat": datetime.now(datetime.timezone.utc),
    }
    encoded_jwt = jwt.encode(data, os.environ.get("JWT_SECRET"), algorithm="HS256")
    return encoded_jwt

def verify_token_jwt(token: str) -> dict:
    """
    Verify a JWT token and return the payload.
    """
    try:
        payload = jwt.decode(token, os.environ.get("JWT_SECRET"), algorithms=["HS256"])
        return payload
    except Exception as e:
        print(f"Token verification failed: {e}")
        return None