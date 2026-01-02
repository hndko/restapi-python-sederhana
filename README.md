# REST API Skeleton (Python Flask) 🚀

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Sebuah template **REST API** yang modern, modular, dan secure, dibangun menggunakan **Flask Framework**. Proyek ini dirancang sebagai fondasi yang kokoh untuk pengembangan backend aplikasi skala kecil hingga menengah, dengan penerapan _Best Practices_ industri.

Repository: [https://github.com/hndko/restapi-python-sederhana](https://github.com/hndko/restapi-python-sederhana)

---

## 👨‍💻 Authors

**Handoko x Mari Partner**

---

## ✨ Key Features

Proyek ini bukan sekadar "Hello World", melainkan implementasi _real-world_ dengan fitur lengkap:

- **Modular Architecture**: Penerapan _Application Factory Pattern_ dan _Blueprints_ untuk kode yang rapi dan mudah di-maintain.
- **Secure Authentication**: Sistem login menggunakan **JWT (JSON Web Token)** dengan validasi Header `Authorization: Bearer`.
- **Database Agnostic**: Support **MySQL** (Production) dan **SQLite** (Development) dengan konfigurasi otomatis via `.env`.
- **Database Migrations**: Manajemen skema database terstruktur menggunakan `Flask-Migrate` (Alembic).
- **Environment Management**: Keamanan data sensitif (API Key, DB Credentials) menggunakan `python-dotenv`.
- **Documentation Ready**: Tersedia **Postman Collection** siap pakai untuk pengujian API.

## 🛠️ Tech Stack

- **Language**: Python 3
- **Framework**: Flask
- **ORM**: Flask-SQLAlchemy
- **Auth**: PyJWT
- **Database Driver**: PyMySQL
- **Utilities**: Flask-Cors, Python-Dotenv

## 🚀 Getting Started

Ikuti langkah berikut untuk menjalankan proyek di mesin lokal Anda.

### 1. Clone Repository

```bash
git clone https://github.com/hndko/restapi-python-sederhana.git
cd restapi-python-sederhana
```

### 2. Setup Environment

Buat file .env dari contoh yang tersedia:

```bash
cp .env.example .env
```

_Edit file `.env` dan sesuaikan konfigurasi database MySQL Anda._

### 3. Install Dependencies

Disarankan menggunakan virtual environment (venv).

```bash
pip install -r requirements.txt
```

### 4. Database Setup (Migrations)

Generate tabel otomatis ke database:

```bash
flask db init      # Hanya dijalankan sekali diawal
flask db migrate   # Jika ada perubahan model
flask db upgrade   # Apply perubahan ke database
```

### 5. Run Application

```bash
python run.py
```

Server akan berjalan di `http://127.0.0.1:5005`.

---

## 📚 API Documentation

Dokumentasi lengkap dan file testing tersedia di folder `docs/`.
Anda dapat mengimport `postman_collection.json` ke aplikasi Postman untuk mencoba endpoint berikut:

| Method   | Endpoint             | Description                  | Auth |
| :------- | :------------------- | :--------------------------- | :--- |
| `POST`   | `/api/auth/register` | Mendaftarkan pengguna baru   | ❌   |
| `POST`   | `/api/auth/login`    | Login & dapatkan Token (JWT) | ❌   |
| `GET`    | `/api/dashboard`     | Contoh halaman protected     | ✅   |
| `GET`    | `/api/people`        | Ambil semua data             | ❌   |
| `POST`   | `/api/people`        | Tambah data baru             | ✅   |
| `PUT`    | `/api/people/<id>`   | Update data                  | ✅   |
| `DELETE` | `/api/people/<id>`   | Hapus data                   | ✅   |

---

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

---

_Built with ❤️ by Handoko x Mari Partner_
