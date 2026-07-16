from flask import render_template

from app.auth import auth_bp
from app.auth.forms import (
    LoginForm,
    RegisterForm
)


@auth_bp.route("/login")
def login():
    form = LoginForm()
    return render_template(
        "auth/login.html",
        form=form
    )

@auth_bp.route("/register")
def register():
    form = RegisterForm()
    return render_template(
        "auth/register.html",
        form=form
    )