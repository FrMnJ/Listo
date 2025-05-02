from fastapi import APIRouter, HTTPException, status

from inter_service_communication import get_user, verify_token
from models import UserRole
from schemas import AuthorizeInput

router = APIRouter()

@router.get("/health", response_model=dict, status_code=status.HTTP_200_OK)
async def health_check() -> dict:
    return {
        "success": True,
        "message": "API is healthy",
        "status": "OK"
    }

@router.post("/authorize", status_code=status.HTTP_200_OK)
async def authorize_user(authorize_input: AuthorizeInput) -> dict:
    user = await verify_token(authorize_input.token)
    print(user)
    if not user[0] or not user[1]:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User not found")
    user = user[1]
    user_roles = await UserRole.filter(user=user["id"]).prefetch_related("role")
    roles = [ur.role for ur in  user_roles]
    for role in roles:
        permissions = await role.permissions.all()
        for permission in permissions:
            if permission.name == (authorize_input.action + " " + authorize_input.object):
                del user["iat"]
                del user["exp"]
                return {
                    "success": True,
                    "message": "User is authorized",
                    "action": authorize_input.action + " " + authorize_input.object,
                    "status": "OK",
                    "user": user,
                }
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="User is not authorized")
    

