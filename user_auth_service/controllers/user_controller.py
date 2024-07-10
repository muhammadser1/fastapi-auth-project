from fastapi import APIRouter, Depends, HTTPException, status
from models.schemas import User
from models.Mysql_database import get_db
from utils.password_utils import hash_password
from utils.password_utils import verify_password
from utils.jwt_manager import generate_jwt
from fastapi.responses import JSONResponse

user_router = APIRouter()


@user_router.get("/welcome/")
def welcome_message():
    return {"message": "Welcome to the User Router"}


@user_router.post("/")
def sign_up(user: User, auth_db=Depends(get_db)):
    """
    Endpoint to register a new user.

    :param user: User object containing user details (username, password, email, role).
    :param auth_db: Dependency to access the database.
    :return: Message indicating successful registration.
    """
    try:
        # Validate the user's role
        if user.role not in ["admin", "user"]:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Role must be 'admin' or 'user'")

        # Check if the username already exists in the database
        existing_user = auth_db.get_user_by_username(user.username)
        if existing_user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already exists")

        # Hash the user's password before storing it
        user.password = hash_password(user.password)

        # Add the user to the database
        auth_db.add_user_to_db(user)

        token_payload = {"sub": user.username, "role": user.role}
        access_token = generate_jwt(token_payload)

        response = JSONResponse(content={"message": "User signed up successfully"})
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to process the request") from e


@user_router.post("/token")
def login_in(username: str, password: str, auth_db=Depends(get_db)):
    """
    Endpoint to authenticate a user

    :param username: Username for authentication.
    :param password: Password for authentication.
    :param auth_db: Dependency to access the database.
    :return: Message indicating successful authentication
    """
    try:
        existing_user = auth_db.get_user_by_username(username)

        if not existing_user:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        if not verify_password(existing_user["password_hash"], password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
        token_payload = {"sub": existing_user["username"], "role": existing_user["role"]}
        access_token = generate_jwt(token_payload)

        response = JSONResponse(content={"message": "User signed in successfully"})
        response.set_cookie(key="access_token", value=access_token, httponly=True)
        return response

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Failed to process the request") from e


@user_router.post("/logout")
def logout():
    """
    Endpoint to log out the current user.
    Clears the access_token cookie to invalidate the session.
    """
    response = JSONResponse(content={"message": "User logged out successfully"})
    response.delete_cookie("access_token")
    return response
