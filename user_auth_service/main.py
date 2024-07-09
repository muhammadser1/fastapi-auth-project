from fastapi import FastAPI, Depends, HTTPException, status
from controllers.user_controller import user_router

app = FastAPI()
app.include_router(user_router,tags=["users"])

@app.get("/")
def test():
    return {"message": "Welcome to the User_Auth Service"}
