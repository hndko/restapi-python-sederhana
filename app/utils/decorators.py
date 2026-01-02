from functools import wraps
from flask import request, jsonify, current_app
import jwt
from ..models.user import User

def token_required(f):
    """
    Decorator untuk memproteksi endpoint yang membutuhkan login.
    Menerima token dari Header 'Authorization: Bearer <token>' atau query param 'token'.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # 1. Cek token di Header Authorization
        if 'Authorization' in request.headers:
            # Format: Bearer <token>
            auth_header = request.headers['Authorization']
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        # 2. Cek token di Query Param (Fallback)
        if not token:
            token = request.args.get('token')

        # 3. Validasi keberadaan token
        if not token:
            return jsonify({'message': 'Token tidak ditemukan! Harap login terlebih dahulu.'}), 401

        try:
            # 4. Decode token
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])

            # 5. Cek validitas user (opsional tapi disarankan)
            # current_user = User.query.filter_by(username=data['username']).first()
            # if not current_user:
            #    return jsonify({'message': 'User tidak valid!'}), 401

        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token sudah kadaluarsa (expired). Silakan login ulang.'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token tidak valid.'}), 401
        except Exception as e:
            return jsonify({'message': 'Terjadi kesalahan pada autentikasi.', 'error': str(e)}), 401

        return f(*args, **kwargs)

    return decorated
