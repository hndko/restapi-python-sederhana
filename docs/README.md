# Dokumentasi API Testing

Folder ini berisi koleksi Postman untuk memudahkan pengujian API.

## Cara Menggunakan Postman Collection

1.  **Install Postman**: Jika belum punya, download dan install [Postman](https://www.postman.com/downloads/).
2.  **Import Collection**:
    - Buka Postman.
    - Klik tombol **Import** di pojok kiri atas.
    - Drag & drop file `postman_collection.json` ke dalam window Import, atau pilih file tersebut.
3.  **Setup Environment (Opsional)**:
    - Collection ini sudah memiliki variabel `base_url` yang diset ke `http://127.0.0.1:5005` secara default.
    - Jika server Anda berjalan di port lain, Anda bisa mengedit variabel ini di tab **Variables** pada Collection setting.
4.  **Testing Alur Auth**:
    - Jalankan request **Auth > Register** terlebih dahulu untuk membuat user.
    - Jalankan request **Auth > Login**. Script otomatis di Postman akan menyimpan `token` yang didapat ke dalam environment variable.
    - Setelah login, Anda bisa langsung menjalankan request di folder **Protected** atau **People CRUD** tanpa perlu copy-paste token manual, karena sudah dihilangkan otomatis lewat `{{token}}`.

## Struktur Collection

- **Auth**: Endpoint registrasi dan login.
- **Public**: Endpoint yang bisa diakses siapa saja.
- **Protected**: Endpoint yang butuh token (contoh: Dashboard).
- **People CRUD**: Operasi Create, Read, Update, Delete untuk data Person.
