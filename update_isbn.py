from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # Daftar ISBN untuk buku-buku kita
    # Format: https://covers.openlibrary.org/b/isbn/ISBN-N-L.jpg (L = Large)
    isbn_map = {
        "Al-Qur'an dan Terjemahannya": "9789791111111",
        "Filosofi Teras": "9786024124981",
        "The Power of Now": "9781577314806",
        "Sapiens: A Brief History of Humankind": "9780062316097",
        "Tasawuf Modern": "9789792323232",
        
        "A Brief History of Time": "9780553380163",
        "Cosmos": "9780345539434",
        "The Selfish Gene": "9780198788607",
        "Kalkulus Jilid 1": "9780130414083",
        "Fisika Dasar untuk Universitas": "9780470469088",

        "Clean Code": "9780132350884",
        "The Pragmatic Programmer": "9780201616224",
        "Artificial Intelligence: A Modern Approach": "9780136042594",
        "Belajar Python dalam 24 Jam": "9780672327193",
        "Hacking: The Art of Exploitation": "9781593271442",

        "Laskar Pelangi": "9789793062792",
        "Bumi Manusia": "9789799731248",
        "Harry Potter and the Philosopher's Stone": "9780747532699",
        "The Hobbit": "9780261102217",
        "Naruto Vol. 1": "9781569319000",

        "Sejarah Indonesia Modern": "9789794618123",
        "Guns, Germs, and Steel": "9780393317558",
        "Manusia dan Kebudayaan di Indonesia": "9789794031234",
        "Napoleon: A Life": "9780143128854",
        "Sejarah Dunia yang Disembunyikan": "9786021234567",

        "Atomic Habits": "9780735211292",
        "The Power of Habit": "9780812981605",
        "Thinking, Fast and Slow": "9780374533557",
        "Man's Search for Meaning": "9780807014295",
        "How to Win Friends and Influence People": "9780671027032",

        "The Psychology of Money": "9780857197689",
        "Rich Dad Poor Dad": "9781612680194",
        "Zero to One": "9780804139298",
        "The Lean Startup": "9780307887894",
        "Ekonomi Pembangunan": "9789791234567",

        "The Art of War": "9781599869773",
        "One Piece Vol. 1": "9781421530531",
        "Dragon Ball Vol. 1": "9781421534393",
        "The Story of Art": "9780714832470",
        "Pengantar Ilmu Komunikasi": "9789791231234",

        "Kamus Besar Bahasa Indonesia (KBBI)": "9789794071234",
        "Metodologi Penelitian Kualitatif": "9786021231234",
        "Ensiklopedia Sains": "9789791231235",
        "Statistika Terapan": "9789791231236",
        "Tata Bahasa Baku Bahasa Indonesia": "9789791231237",

        "Why We Sleep": "9781501144318",
        "How Not to Die": "9781250066114",
        "Buku Pintar Kesehatan Keluarga": "9789791231238",
        "The 4-Hour Body": "9780307463630",
        "Nutrisi Sehat untuk Keluarga": "9789791231239",
    }

    updated_count = 0
    for title, isbn in isbn_map.items():
        book = Book.query.filter_by(title=title).first()
        if book:
            # Link Open Library berdasarkan ISBN
            book.cover_image = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
            updated_count += 1

    db.session.commit()
    print(f"✅ Berhasil memperbarui {updated_count} sampul buku dengan link ISBN yang stabil!")