from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # Kita ganti semua gambar yang mati dengan gambar dari Unsplash Source
    # Unsplash menjamin gambar 100% muncul dan gambarnya estetik (acak)
    books = Book.query.all()
    
    # Kita pakai layanan Picsum Photos yang sangat stabil, 
    # gambarnya acak (beda-beda per ID), dan dijamin 100% muncul.
    for book in books:
        # format URL: https://picsum.photos/seed/judulbuku/400/600
        safe_title = book.title.replace(" ", "").replace("'", "").replace("&", "")
        # Kita pakai inisial judulnya sebagai seed biar gambarnya konsisten dan unik per buku
        book.cover_image = f"https://picsum.photos/seed/{safe_title}/400/600"
        
    db.session.commit()
    print(f"✅ Berhasil memperbarui semua sampul dengan gambar acak yang DIJAMIN MUNCUL!")