from flask import render_template

from flask_login import login_required

from app.favorites import favorites_bp


@favorites_bp.route("/")
@login_required
def index():

    return render_template(
        "favorites/index.html"
    )