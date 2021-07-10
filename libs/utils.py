import re
from passlib.hash import pbkdf2_sha512

class Utils:
    @staticmethod
    def email_is_valid(email: str) -> bool:
        email_matcher = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        return True if email_matcher.match(email) else False

    @staticmethod
    def login_is_valid(email: str, password: str):
        pass

    @staticmethod
    def hash_password(password: str) -> str:
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_password(password: str, hash_password: str) -> bool:
        return pbkdf2_sha512.verify(password, hash_password)



