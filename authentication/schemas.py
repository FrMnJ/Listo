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

class VerifyToken(BaseModel):
    token: str

class UserOut(BaseModel):
    id: int
    username: str
    full_name: str
    email: EmailStr
    phone_number: str
    address: str
    last_login: str | None = None
    is_verified: bool = False
    language: str = 'en'
    utm_source: str = "Other"
    device_used: str | None = None
    location: str | None = None
    url_profile: str | None = None
    url_drive_license: str | None = None
    url_identification: str | None = None
    deleted_at: str | None = None

    class Config:
        orm_mode = True

