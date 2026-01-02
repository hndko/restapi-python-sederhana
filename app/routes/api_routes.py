from flask import Blueprint, request, jsonify
from ..models.person import Person
from ..utils.decorators import token_required

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/dashboard', methods=['GET'])
@token_required
def dashboard():
    """
    Halaman Dashboard (Protected).
    Hanya bisa diakses jika memiliki token valid.
    """
    return jsonify({"message": "Selamat datang di Dashboard! Token Anda valid."})

@api_bp.route('/', methods=['GET'])
def index():
    """Halaman Public"""
    return jsonify({"message": "Ini adalah halaman publik. Silakan login di /api/auth/login"})

# --- CRUD Person ---

@api_bp.route('/people', methods=['GET'])
def get_people():
    """Mendapatkan semua data orang."""
    people = Person.query.all()
    output = [person.to_dict() for person in people]

    return jsonify({
        "status": 200,
        "message": "Berhasil mengambil data",
        "data": output
    })

@api_bp.route('/people', methods=['POST'])
@token_required # Opsional: Proteksi create data
def create_person():
    """Menambahkan data orang baru."""
    data = request.get_json() or request.form

    nama = data.get('nama')
    umur = data.get('umur')
    alamat = data.get('alamat')

    if not nama or not umur:
        return jsonify({"message": "Nama dan Umur wajib diisi!"}), 400

    person = Person(nama=nama, umur=umur, alamat=alamat)

    if person.save():
        return jsonify({
            "status": 200,
            "message": "Data berhasil ditambahkan",
            "data": person.to_dict()
        }), 201
    else:
        return jsonify({"message": "Gagal menyimpan data"}), 500

@api_bp.route('/people/<int:id>', methods=['PUT'])
@token_required
def update_person(id):
    """Mengupdate data orang berdasarkan ID."""
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Data tidak ditemukan"}), 404

    data = request.get_json() or request.form

    person.nama = data.get('nama', person.nama)
    person.umur = data.get('umur', person.umur)
    person.alamat = data.get('alamat', person.alamat)

    if person.save():
        return jsonify({
            "status": 200,
            "message": "Data berhasil diupdate",
            "data": person.to_dict()
        })
    else:
        return jsonify({"message": "Gagal update data"}), 500

@api_bp.route('/people/<int:id>', methods=['DELETE'])
@token_required
def delete_person(id):
    """Menghapus data orang berdasarkan ID."""
    person = Person.query.get(id)
    if not person:
        return jsonify({"message": "Data tidak ditemukan"}), 404

    if person.delete():
        return jsonify({
            "status": 200,
            "message": "Data berhasil dihapus"
        })
    else:
        return jsonify({"message": "Gagal menghapus data"}), 500
