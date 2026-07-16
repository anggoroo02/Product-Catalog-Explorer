import requests

from flask import current_app


def _request(endpoint):

    base_url = current_app.config["FAKESTORE_API_BASE_URL"]

    url = f"{base_url}{endpoint}"

    response = requests.get(
        url,
        timeout=current_app.config["REQUEST_TIMEOUT"]
    )

    response.raise_for_status()

    return response.json()


def get_all_products():

    return _request("/products")


def get_product_by_id(product_id):

    return _request(
        f"/products/{product_id}"
    )


def get_categories():

    return _request(
        "/products/categories"
    )


def get_products_by_category(category):

    return _request(
        f"/products/category/{category}"
    )