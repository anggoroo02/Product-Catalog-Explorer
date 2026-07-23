from typing import Optional, Tuple

from sqlalchemy import or_

from app.extensions import db
from app.models import User


def get_user_by_id(user_id: int) -> Optional[User]:
    return db.session.get(User, user_id)


def get_user_by_username(username: str) -> Optional[User]:
    return User.query.filter_by(username=username).first()


def get_user_by_email(email: str) -> Optional[User]:
    return User.query.filter_by(email=email).first()


def register_user(
    username: str,
    email: str,
    password: str
) -> Tuple[Optional[User], Optional[str]]:
    username = username.strip()
    email = email.strip()

    if get_user_by_username(username):
        return None, "username_taken"

    if get_user_by_email(email):
        return None, "email_taken"

    user = User(
        username=username,
        email=email
    )
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return user, None


def authenticate_user(
    identifier: str,
    password: str
) -> Optional[User]:
    identifier = identifier.strip()

    user = User.query.filter(
        or_(
            User.username == identifier,
            User.email == identifier
        )
    ).first()

    if user is None or not user.check_password(password):
        return None

    return user
