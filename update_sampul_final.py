from app import create_app, db
from app.models import Book
from urllib.parse import quote

app = create_app()

with app.app_context():
    books = Book.query.all()
    updated_count = 0

    for book in books:
        # Kita pakai layanan placehold.co yang otomatis menampilkan judul buku
        # Warna latar belakang gelap (2a2a38) dan teks ungu (7c5cff) agar cocok dengan tema
        safe_title = quote(book.title)
        # Format URL: https://placehold.co/400x600/2a2a38/7c5cff?text=Judul+Buku
        new_cover_url = f"https://placehold.co/400x600/2a2a38/7c5cff?text={safe_title}"
        
        book.cover_image = new_cover_url
        updated_count += 1

    db.session.commit()
    print(f"✅ Berhasil memperbarui {updated_count} sampul buku menjadi gambar otomatis yang pasti muncul!")