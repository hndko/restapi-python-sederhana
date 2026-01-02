from ..extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    """
    Model Database untuk data Pengguna (User).
    Digunakan untuk autentikasi.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)

    def set_password(self, password):
        """Mengatur password dengan hashing."""
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """Memeriksa apakah password cocok."""
        return check_password_hash(self.password_hash, password)

    def save(self):
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error saving user: {e}")
            db.session.rollback()
            return False
