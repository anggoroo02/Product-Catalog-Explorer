from flask import (
    render_template,
    redirect,
    url_for,
    flash
)
from app.auth import auth_bp
from app.auth.forms import (
    LoginForm,
    RegisterForm
)
from app.extensions import db
from app.models import User


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    return render_template(
        "auth/login.html",
        form=form
    )

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    return render_template(
        "auth/register.html",
        form=form
    )