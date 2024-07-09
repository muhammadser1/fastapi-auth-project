from fastapi import APIRouter, Depends, HTTPException, status


user_router = APIRouter()
@user_router.get("/welcome/")
def welcome_message():
    return {"message": "Welcome to the User Router"}
