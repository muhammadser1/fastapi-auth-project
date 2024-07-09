import bcrypt


def hash_password(password: str):
    if not isinstance(password, str):
        raise TypeError("Password must be a string")
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword.decode('utf-8')


def verify_password(stored_pass:str, user_pass:str):
    if not isinstance(stored_pass, str):
        raise TypeError("Password must be a string")
    if not isinstance(user_pass, str):
        raise TypeError("Password must be a string")
    return bcrypt.checkpw(user_pass.encode('utf-8'), stored_pass.encode('utf-8'))