import os

class Config:
    # Mengambil path direktori base
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))

    # Konfigurasi Database SQLite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret Key untuk session dan JWT (Ganti 'inirahasianegara' dengan key yang aman di production)
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'inirahasianegara'
