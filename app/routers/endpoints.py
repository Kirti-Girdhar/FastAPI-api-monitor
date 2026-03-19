from fastapi import APIRouter, Depends, HTTPException, status
from app.utils.dependencies import get_current_user 

router = APIRouter(
    prefix="/endpoints"
)

@router.get("/protected")
def protected(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user.email}"}

