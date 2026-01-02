from flask import Flask
from .extensions import db, cors
from config import Config

def create_app(config_class=Config):
    # Inisialisasi aplikasi Flask
    app = Flask(__name__)

    # Memuat konfigurasi dari object Config
    app.config.from_object(config_class)

    # Inisialisasi extension dengan app instance
    db.init_app(app)
    cors.init_app(app)

    # Import dan register blueprint (akan ditambahkan nanti)
    from .routes.api_routes import api_bp
    from .routes.auth_routes import auth_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    # Membuat tabel database jika belum ada (opsional, sebaiknya pakai Flask-Migrate di production)
    with app.app_context():
        db.create_all()

    return app
