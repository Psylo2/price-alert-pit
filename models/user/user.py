import uuid
from dataclasses import dataclass, field
from typing import Dict

from models.abc.model import Model
from libs.utils import Utils
import models.user.errors as UserErrors

@dataclass
class User(Model):
    _collection: str = field(init=False, default="users")
    email: str
    password: str = field(repr=False)
    _id: str = field(default_factory=lambda: uuid.uuid4().hex)

    @classmethod
    def find_by_email(cls, email: str) -> "User":
        try:
            return cls.find_one_by('email', email)
        except TypeError:
            raise UserErrors.UserNotFoundError('A user with this e-mail was not found')

    @classmethod
    def register_user(cls, email: str, password: str) -> bool:
        if not Utils.email_is_valid(email):
            raise UserErrors.InvalidEmailError('the e-mail does not have the right format')

        try:
            cls.find_by_email(email)
            raise UserErrors.UserAlreadyRegisteredError('The e-mail you used to register already exists.')
        except UserErrors.UserNotFoundError:
            User(email,
                 Utils.hash_password(password)
                 ).save_to_mongo()

        return True

    @classmethod
    def valid_login(cls, email: str, password: str):
        user = cls.find_by_email(email)

        if not Utils.check_password(password, user.password):
            raise UserErrors.IncorrectPassword('Your password is incorrect')

        return True


    def json(self) -> Dict:
        return {
            '_id': self._id,
            'email': self.email,
            'password': self.password
        }
