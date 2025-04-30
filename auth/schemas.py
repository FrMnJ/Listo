from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    full_name: str
    email: EmailStr
    phone_number: str
    address: str
    password: str
    language: str = 'en'
    utm_source: str = "Other"
    device_used: str | None = None
    location: str | None = None

class UserLogin(BaseModel):
    email: str
    password: str