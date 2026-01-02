import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Mengambil path direktori base
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Ambil credential database dari environment variable
    DB_USERNAME = os.getenv('DB_USERNAME', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
    DB_PORT = os.getenv('DB_PORT', '3306')
    DB_NAME = os.getenv('DB_NAME', 'restapi_python')

    # Konfigurasi Database (MySQL)
    # Jika variabel env tidak lengkap, fallback ke SQLite
    if DB_USERNAME and DB_NAME:
        # mysql+pymysql://user:password@host:port/dbname
        SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    else:
        # Fallback to SQLite
        SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret Key untuk session dan JWT
    SECRET_KEY = os.getenv('SECRET_KEY', 'inirahasianegara')
