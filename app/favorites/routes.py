from flask import (
    render_template,
    redirect,
    url_for,
    flash
)

from flask_login import (
    login_required,
    current_user
)

from app.favorites import favorites_bp

from app.services.favorite_service import (
    add_favorite,
    remove_favorite,
    get_user_favorites
)

from app.services.product_service import (
    get_product_by_id
)


@favorites_bp.route("")
@login_required
def index():

    favorites = get_user_favorites(
        current_user.id
    )

    products = []

    for favorite in favorites:

        product = get_product_by_id(
            favorite.product_id
        )

        if product is not None:
            products.append(product)

    return render_template(
        "favorites/index.html",
        products=products
    )


@favorites_bp.route(
    "/add/<int:product_id>",
    methods=["POST"]
)
@login_required
def add(product_id):

    success = add_favorite(
        current_user.id,
        product_id
    )

    if success:

        flash(
            "Produk berhasil ditambahkan ke favorite.",
            "success"
        )

    else:

        flash(
            "Produk sudah ada di favorite.",
            "warning"
        )

    return redirect(
        url_for(
            "products.detail",
            product_id=product_id
        )
    )


@favorites_bp.route(
    "/remove/<int:product_id>",
    methods=["POST"]
)
@login_required
def remove(product_id):

    success = remove_favorite(
        current_user.id,
        product_id
    )

    if success:

        flash(
            "Produk berhasil dihapus dari favorite.",
            "success"
        )

    else:

        flash(
            "Produk tidak ditemukan di favorite.",
            "warning"
        )

    return redirect(
        url_for(
            "products.detail",
            product_id=product_id
        )
    )