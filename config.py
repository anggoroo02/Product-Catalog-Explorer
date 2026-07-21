import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    FAKESTORE_API_BASE_URL = os.getenv(
        "FAKESTORE_API_BASE_URL"
    )

    REQUEST_TIMEOUT = 10