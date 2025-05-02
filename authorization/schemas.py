from pydantic import BaseModel
class AuthorizeInput(BaseModel):
    token: str
    action: str
    object: str