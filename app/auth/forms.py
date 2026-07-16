# RegisterForm
from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    SubmitField
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length
)


class RegisterForm(FlaskForm):

    username = StringField(
        "Username",
        validators=[
            DataRequired(),
            Length(min=3, max=50)
        ]
    )

    email = StringField(
        "Email",
        validators=[
            DataRequired(),
            Email(),
            Length(max=120)
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Length(min=8)
        ]
    )

    confirm_password = PasswordField(
        "Konfirmasi Password",
        validators=[
            DataRequired(),
            EqualTo(
                "password",
                message="Password tidak sama."
            )
        ]
    )

    submit = SubmitField("Register")

# LoginForm
class LoginForm(FlaskForm):

    username_or_email = StringField(
        "Username atau Email",
        validators=[
            DataRequired()
        ]
    )

    password = PasswordField(
        "Password",
        validators=[
            DataRequired()
        ]
    )

    remember_me = BooleanField(
        "Remember Me"
    )

    submit = SubmitField("Login")