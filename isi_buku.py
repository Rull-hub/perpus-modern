from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # Daftar buku yang mau dimasukkan
    daftar_buku = [
        {
            "title": "Laskar Pelangi", "author": "Andrea Hirata", "category": "Novel",
            "synopsis": "Kisah 10 anak Belitung yang bersekolah di SD Muhammadiyah.",
            "cover_image": "https://covers.openlibrary.org/b/id/8739161-M.jpg", "stock": 5
        },
        {
            "title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "category": "Sejarah",
            "synopsis": "Kisah Minke di akhir era kolonialisme Belanda.",
            "cover_image": "https://covers.openlibrary.org/b/id/13279123-M.jpg", "stock": 3
        },
        {
            "title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "category": "Fantasi",
            "synopsis": "Petualangan pertama Harry Potter di Hogwarts.",
            "cover_image": "https://covers.openlibrary.org/b/id/7984916-M.jpg", "stock": 10
        },
        {
            "title": "Naruto Vol. 1", "author": "Masashi Kishimoto", "category": "Manga",
            "synopsis": "Awal mula perjalanan ninja Naruto Uzumaki.",
            "cover_image": "https://covers.openlibrary.org/b/id/10046027-M.jpg", "stock": 8
        },
        {
            "title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fantasi",
            "synopsis": "Perjalanan Bilbo Baggins mencari harta karun para kurcaci.",
            "cover_image": "https://covers.openlibrary.org/b/id/8406786-M.jpg", "stock": 4
        },
        {
            "title": "Filosofi Teras", "author": "Henry Manampiring", "category": "Pengembangan Diri",
            "synopsis": "Pengenalan filsafat Stoa untuk kehidupan modern.",
            "cover_image": "https://covers.openlibrary.org/b/id/10501234-M.jpg", "stock": 6
        }
    ]

    # Memasukkan ke database
    for b in daftar_buku:
        # Cek biar nggak dobel masukinnya
        if not Book.query.filter_by(title=b["title"]).first():
            buku_baru = Book(**b)
            db.session.add(buku_baru)

    db.session.commit()
    print("✅ Berhasil! 6 Buku Dummy sudah masuk ke database!")