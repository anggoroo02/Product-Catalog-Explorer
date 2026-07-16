from flask import Flask, redirect, url_for

from config import Config

from app.extensions import (
    db,
    login_manager,
    migrate
)

from app.auth import auth_bp
from app.dashboard import dashboard_bp


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inisialisasi extension
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Import model agar dikenali SQLAlchemy
    from app import models

    # Register blueprint
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)

    # Route root
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    return app