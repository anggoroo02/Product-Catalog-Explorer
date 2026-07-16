from flask import (
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_user,
    logout_user,
    login_required
)

from sqlalchemy import or_

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

    if form.validate_on_submit():

        identifier = form.username_or_email.data.strip()

        user = User.query.filter(
            or_(
                User.username == identifier,
                User.email == identifier
            )
        ).first()

        if user is None or not user.check_password(form.password.data):

            flash(
                "Username/email atau password salah.",
                "danger"
            )

            return render_template(
                "auth/login.html",
                form=form
            )

        login_user(
            user,
            remember=form.remember_me.data
        )

        flash(
            f"Selamat datang, {user.username}!",
            "success"
        )

        return redirect(
            url_for("dashboard.index")
        )

    return render_template(
        "auth/login.html",
        form=form
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    form = RegisterForm()

    if form.validate_on_submit():

        existing_username = User.query.filter_by(
            username=form.username.data.strip()
        ).first()

        if existing_username:

            flash(
                "Username sudah digunakan.",
                "danger"
            )

            return render_template(
                "auth/register.html",
                form=form
            )

        existing_email = User.query.filter_by(
            email=form.email.data.strip()
        ).first()

        if existing_email:

            flash(
                "Email sudah digunakan.",
                "danger"
            )

            return render_template(
                "auth/register.html",
                form=form
            )

        user = User(
            username=form.username.data.strip(),
            email=form.email.data.strip()
        )

        user.set_password(
            form.password.data
        )

        db.session.add(user)
        db.session.commit()

        flash(
            "Registrasi berhasil. Silakan login.",
            "success"
        )

        return redirect(
            url_for("auth.login")
        )

    return render_template(
        "auth/register.html",
        form=form
    )


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    flash(
        "Berhasil logout.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )