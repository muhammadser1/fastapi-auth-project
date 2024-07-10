from fastapi import APIRouter, Depends, HTTPException, status, Request
from utils.jwt_manager import check_user_token

user_router = APIRouter()


@user_router.get("/welcome/user/")
def welcome_message(role: str = Depends(check_user_token)):
    return {"message": f"Welcome to the user Router, your role is {role}"}
