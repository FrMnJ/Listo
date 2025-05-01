import os
from passlib.context import CryptContext
from models import User
import jwt
from datetime import datetime, timedelta, timezone
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
    encoded_jwt = jwt.encode(user.dict(), str(os.environ.get("JWT_SECRET", "secret")), algorithm="HS256")
    return encoded_jwt

def verify_token_jwt(token: str) -> dict:
    """
    Verify a JWT token and return the payload.
    """
    try:
        payload = jwt.decode(token, os.environ.get("JWT_SECRET", "secret"), algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        raise e