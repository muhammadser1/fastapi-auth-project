import time
import jwt
from fastapi import HTTPException, status, Request

jwt_secret = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algorithm = "HS256"


def verify_jwt(user_jwt: str):
    try:
        decoded_token = jwt.decode(user_jwt, jwt_secret, algorithms=["HS256"])
        return decoded_token["role"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")


def check_all_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing access token")
    result = verify_jwt(token)
    print(result)
    return result


def check_user_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing access token")
    role = verify_jwt(token)
    print(role)
    if role != "user":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied: User role required")
    return role


def check_admin_token(request: Request) -> str:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing access token")
    role = verify_jwt(token)
    if role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Permission denied: Admin role required")
    return role
