import os

POSTGRES_CONNECTION = os.getenv("POSTGRES_CONNECTION", "")
FLASK_ENV = os.getenv("FLASK_ENV", "production")