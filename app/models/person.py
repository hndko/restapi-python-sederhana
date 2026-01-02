from ..extensions import db

class Person(db.Model):
    """
    Model Database untuk menyimpan data orang (Person).
    """
    __tablename__ = 'people' # Menentukan nama tabel secara eksplisit

    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    umur = db.Column(db.Integer, nullable=False)
    alamat = db.Column(db.Text, nullable=True)

    def save(self):
        """
        Menyimpan data ke database.
        Returns:
            bool: True jika berhasil, False jika gagal.
        """
        try:
            db.session.add(self)
            db.session.commit()
            return True
        except Exception as e:
            # Sebaiknya log error di sini
            print(f"Error saving data: {e}")
            db.session.rollback()
            return False

    def delete(self):
        """
        Menghapus data dari database.
        """
        try:
            db.session.delete(self)
            db.session.commit()
            return True
        except Exception as e:
            print(f"Error deleting data: {e}")
            db.session.rollback()
            return False

    def to_dict(self):
        """
        Mengubah object menjadi dictionary untuk JSON response.
        """
        return {
            "id": self.id,
            "nama": self.nama,
            "umur": self.umur,
            "alamat": self.alamat
        }
