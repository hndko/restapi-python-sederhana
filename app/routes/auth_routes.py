from flask import Blueprint, request, jsonify, current_app
from ..models.user import User
from ..extensions import db
import jwt
import datetime

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Endpoint untuk mendaftarkan user baru.
    """
    try:
        data = request.get_json() or request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username dan password wajib diisi!'}), 400

        # Cek apakah user sudah ada
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username sudah terdaftar!'}), 409

        new_user = User(username=username)
        new_user.set_password(password)

        if new_user.save():
            return jsonify({'message': 'Registrasi berhasil!'}), 201
        else:
            return jsonify({'message': 'Gagal menyimpan user.'}), 500

    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan internal.', 'error': str(e)}), 500

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Endpoint untuk login dan mendapatkan token JWT.
    """
    try:
        # Support JSON body dan Form data
        data = request.get_json() or request.form
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return jsonify({'message': 'Username dan password wajib diisi!'}), 400

        user = User.query.filter_by(username=username).first()

        # Verifikasi user dan password
        if user and user.check_password(password):
            # Generate JWT Token (Berlaku 10 menit)
            expiration = datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
            token = jwt.encode(
                {
                    'username': user.username,
                    'exp': expiration
                },
                current_app.config['SECRET_KEY'],
                algorithm="HS256"
            )

            # Jika encoded token berupa bytes (tergantung versi PyJWT), decode ke string
            if isinstance(token, bytes):
                token = token.decode('utf-8')

            return jsonify({
                'message': 'Login berhasil!',
                'token': token,
                'expires_in': '60 minutes'
            }), 200

        return jsonify({'message': 'Username atau password salah!'}), 401

    except Exception as e:
        return jsonify({'message': 'Terjadi kesalahan internal.', 'error': str(e)}), 500
