from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Silakan login untuk mengakses halaman."

# Note: CSRFProtect dari Flask-WTF juga bisa kita tambahkan di sini pada tahap berikutnya agar seluruh form otomatis terlindungi CSRF