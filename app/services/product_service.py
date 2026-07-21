import requests

from flask import current_app
from requests.exceptions import (
    Timeout,
    ConnectionError,
    HTTPError,
    RequestException
)


def _request(endpoint):

    base_url = current_app.config["FAKESTORE_API_BASE_URL"]

    url = f"{base_url}{endpoint}"

    try:

        response = requests.get(
            url,
            timeout=current_app.config["REQUEST_TIMEOUT"]
        )

        response.raise_for_status()

        return response.json()

    except Timeout:

        current_app.logger.error(
            "FakeStore API timeout."
        )

    except ConnectionError:

        current_app.logger.error(
            "Tidak dapat terhubung ke FakeStore API."
        )

    except HTTPError as e:

        current_app.logger.error(
            f"HTTP Error: {e}"
        )

    except RequestException as e:

        current_app.logger.error(
            f"Request Error: {e}"
        )

    return None


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