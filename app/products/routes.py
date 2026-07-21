from flask import (
    render_template,
    flash,
    redirect,
    url_for
)

from flask_login import (
    login_required,
    current_user
)

from app.products import products_bp

from app.services import product_service
from app.services.favorite_service import (
    is_favorite
)
from app.services.note_service import (
    get_product_notes
)


@products_bp.route("")
@login_required
def index():

    products = product_service.get_all_products()

    if products is None:

        flash(
            "Gagal mengambil data produk dari server.",
            "danger"
        )

        products = []

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

    if product is None:

        flash(
            "Produk tidak dapat ditemukan.",
            "danger"
        )

        return redirect(
            url_for("products.index")
        )

    favorite = is_favorite(
        current_user.id,
        product_id
    )

    notes = get_product_notes(
        current_user.id,
        product_id
    )

    return render_template(
        "products/detail.html",
        product=product,
        favorite=favorite,
        notes=notes
    )