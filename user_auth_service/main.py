from fastapi import FastAPI, Depends, HTTPException, status
app = FastAPI()

@app.get("/")
def test():
    return {"message": "Welcome to the User_Auth Service"}
