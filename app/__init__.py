from flask import Flask

from config import Config
from app.extensions import (
    db,
    login_manager,
    migrate
)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi extension
    from app import models
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Route sementara untuk memastikan aplikasi berjalan
    @app.route("/")
    def index():
        return """
        <h1>Product Catalog Explorer</h1>
        <p>Flask is Running!</p>
        """

    return app