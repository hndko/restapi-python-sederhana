from flask import Flask
from .extensions import db, cors, migrate
from config import Config

def create_app(config_class=Config):
    # Inisialisasi aplikasi Flask
    app = Flask(__name__)

    # Memuat konfigurasi dari object Config
    app.config.from_object(config_class)

    # Inisialisasi extension dengan app instance
    db.init_app(app)
    cors.init_app(app)
    migrate.init_app(app, db) # Inisialisasi Migrations

    # Import dan register blueprint
    from .routes.api_routes import api_bp
    from .routes.auth_routes import auth_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(auth_bp)

    # Register CLI Commands
    # Import di dalam fungsi untuk menghindari circular import jika ada
    try:
        from .cli import seed_command
        app.cli.add_command(seed_command)
    except ImportError as e:
        print(f"Warning: Could not register seed command: {e}")

    return app
