from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from flask_migrate import Migrate

# Inisialisasi object SQLAlchemy
db = SQLAlchemy()

# Inisialisasi object Migrate
migrate = Migrate()

# Inisialisasi object CORS
cors = CORS()
