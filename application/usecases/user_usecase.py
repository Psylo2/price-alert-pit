from flask import session, flash
import uuid
from typing import Union, Dict

from infrastructure.repositories.services import RepositoryServices
from application.core.password_encryption import hash_password, check_password
from application.usecases.services import UserUseCaseService
from domain.models import UserModel


class UserUseCase(UserUseCaseService):

    def __init__(self, repository_service: RepositoryServices):
        self._repository = repository_service

    def user_register(self, email: str, password: str) -> bool:
        if self._find_user_by_email(email=email):
            flash('Given e-mail already exists.')
            return False

        self._register_user(email=email, password=password)
        return True

    def user_login(self, email: str, password: str) -> bool:
        user = self._find_user_by_email(email=email)
        if not self._valid_user_login(user=user, password=password):
            return False

        return True

    def user_logout(self) -> None:
        session['email'] = None

    def _register_user(self, email: str, password: str) -> None:
        user_id = uuid.uuid4()
        password = hash_password(password=password)
        user_model = UserModel(user_id=user_id, email=email, password=password)
        self._repository.insert(user_model.dict())

    def _valid_user_login(self, user: Dict, password: str) -> bool:
        if not user:
            flash('User Not Found')
            return False
        return self._validate_user_login(user=user, password=password)

    def _validate_user_login(self, user: Dict, password: str) -> bool:
        user_validated = UserModel(**user)
        if not check_password(password, user_validated.password):
            flash('Your password is incorrect')
            return False
        session['email'] = user_validated.email
        return True

    def _find_user_by_email(self, email: str) -> Union[Dict, None]:
        user = self._repository.find_one({"email": email})
        return user
