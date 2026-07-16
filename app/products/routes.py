from flask import render_template

from flask_login import login_required

from app.products import products_bp


@products_bp.route("/")
@login_required
def index():

    return render_template(
        "products/index.html"
    )