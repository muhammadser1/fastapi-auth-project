import time
import jwt
jwt_secret = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
algorithm = "HS256"


def generate_jwt(payload, expiration_time=60):
    payload['exp'] = int(time.time()) + expiration_time
    encoded_jwt = jwt.encode(payload, jwt_secret, algorithm=algorithm)
    return encoded_jwt
