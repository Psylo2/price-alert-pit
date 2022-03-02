from passlib.hash import pbkdf2_sha512


def hash_password(password: str) -> str:
    return pbkdf2_sha512.encrypt(password)


def check_password(password: str, hashpassword: str) -> bool:
    return pbkdf2_sha512.verify(password, hashpassword)
