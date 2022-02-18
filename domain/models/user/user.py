import re
from pydantic import BaseModel, validator


class UserModel(BaseModel):
    user_id: str
    email: str
    password: str

    @validator('user_id', 'password')
    def validate_string(cls, str_):
        if not isinstance(str_, type(str)):
            raise TypeError("type must be string")
        return str_

    @validator('email', allow_reuse=True)
    def validate_string(cls, str_):
        if not isinstance(str_, type(str)):
            raise TypeError("type must be string")
        email_validation = re.compile(r"^[\w-]+@([\w]+\.)+[\w]+[\.+A-Za-z{2,}]+$")
        if not email_validation.match(str_):
            raise Exception("email not match complexity")
        return str_

