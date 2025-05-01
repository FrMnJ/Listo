from fastapi import APIRouter, HTTPException, status

router = APIRouter()

@router.get("/health", response_model=dict, status_code=status.HTTP_200_OK)
async def health_check() -> dict:
    return {
        "success": True,
        "message": "API is healthy",
        "status": "OK"
    }
