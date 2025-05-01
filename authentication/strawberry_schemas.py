import strawberry 
from typing import Optional

@strawberry.type
class UserType:
    id: int
    username: str
    full_name: str
    email: str
    phone_number: str
    address: str
    last_login: Optional[str] = None
    is_verified: bool
    language: str
    utm_source: str
    device_used: Optional[str] = None
    location: Optional[str] = None
    url_profile: Optional[str] = None
    url_drive_license: Optional[str] = None
    url_identification: Optional[str] = None
    deleted_at: Optional[str] = None