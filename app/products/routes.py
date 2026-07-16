from flask import render_template

from flask_login import login_required

from app.products import products_bp

from app.services.product_service import (
    get_all_products
)


@products_bp.route("/")
@login_required
def index():

    products = get_all_products()

    return render_template(
        "products/index.html",
        products=products
    )