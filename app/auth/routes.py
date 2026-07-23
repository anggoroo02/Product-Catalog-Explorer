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

from app.auth import auth_bp
from app.auth.forms import (
    LoginForm,
    RegisterForm
)
from app.services.auth_service import (
    authenticate_user,
    register_user
)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    form = LoginForm()

    if form.validate_on_submit():
        user = authenticate_user(
            form.username_or_email.data,
            form.password.data
        )

        if user is None:

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
        user, error = register_user(
            form.username.data,
            form.email.data,
            form.password.data
        )

        if error == "username_taken":

            flash(
                "Username sudah digunakan.",
                "danger"
            )

            return render_template(
                "auth/register.html",
                form=form
            )

        if error == "email_taken":

            flash(
                "Email sudah digunakan.",
                "danger"
            )

            return render_template(
                "auth/register.html",
                form=form
            )

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
