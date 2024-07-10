from fastapi import APIRouter, Depends, HTTPException, status
from utils.jwt_manager import check_admin_token

admin_router = APIRouter()


@admin_router.get("/welcome/admin/")
def welcome_message(role: str = Depends(check_admin_token)):
    return {"message": "Welcome to the admin Router"}

