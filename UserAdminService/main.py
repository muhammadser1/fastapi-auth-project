from fastapi import FastAPI, Depends, HTTPException, status
from controllers.admin import admin_router
from controllers.user import user_router

app = FastAPI()
app.include_router(admin_router,tags=["admin"])
app.include_router(user_router,tags=["admin"])

@app.get("/")
def test():
    return {"message": "Welcome to the User_Auth Service"}
