from functools import wraps
from flask import abort
from flask_jwt_extended import (
    create_access_token, create_refresh_token, get_jwt_identity,
    verify_jwt_in_request
)

from database.user import UserTool
from untity.encry import encrypt

class AuthenticationError(Exception):
    """Base Authentication Exception"""
    def __init__(self, msg=None):
        self.msg = msg

    def __str__(self):
        return self.__class__.__name__ + '(' + str(self.msg) + ')'


class InvalidCredentials(AuthenticationError):
    """Invalid username/password"""


class AccountInactive(AuthenticationError):
    """Account is disabled"""


class AccessDenied(AuthenticationError):
    """Access is denied"""


class UserNotFound(AuthenticationError):
    """User identity not found"""


def authenticate_user(username, password):

    tuser = UserTool.get_user(username)

    if username == tuser.username and encrypt.verify_hash(password, tuser.password):
        if tuser.enable:
            return (
                create_access_token(identity=username),
                create_refresh_token(identity=username)
            )
        else:
            raise AccountInactive(username)


def get_authenticated_user():

    identity = get_jwt_identity()
    alluser = UserTool.get_all_user() 

    for user in alluser:
        if identity == user[0]:
            if user[1]:
                return user
            else:
                raise AccountInactive()
    else:
        raise UserNotFound(identity)


def deauthenticate_user():
    
    identity = get_jwt_identity()

def auth_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        verify_jwt_in_request()

        try:
            get_authenticated_user()

            return func(*args, **kwargs)
        except (UserNotFound, AccountInactive) as error:
            abort(403)

    return wrapper


def auth_refresh_required(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        #verify_jwt_refresh_token_in_request()
        try:
            get_authenticated_user()
            return func(*args, **kwargs)
        except:
            abort(403)

    return wrapper

