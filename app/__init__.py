from flask import Flask

from config import Config
from app.extensions import (
    db,
    login_manager,
    migrate
)
from app.auth import auth_bp
from flask import redirect, url_for

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
        return redirect(url_for("auth.login"))
    
    app.register_blueprint(auth_bp)

    return app