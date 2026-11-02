from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    books = Book.query.all()
    for book in books:
        book.cover_image = None # Kita kosongkan gambar aslinya
    db.session.commit()
    print("✅ Semua link gambar lama berhasil dihapus. Sistem akan membuat sampul otomatis!")