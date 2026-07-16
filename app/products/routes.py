from flask import render_template

from flask_login import login_required

from app.products import products_bp

from app.services import product_service


@products_bp.route("")
@login_required
def index():

    products = product_service.get_all_products()

    return render_template(
        "products/index.html",
        products=products
    )


@products_bp.route("/<int:product_id>")
@login_required
def detail(product_id):

    product = product_service.get_product_by_id(
        product_id
    )

    return render_template(
        "products/detail.html",
        product=product
    )