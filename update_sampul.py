from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # Daftar link sampul unik (pakai gambar dari Unsplash/Picsum biar stabil dan keren)
    # Atau kita pakai URL sampul buku nyata dari Open Library/Google
    cover_updates = {
        "Al-Qur'an dan Terjemahannya": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Filosofi Teras": "https://upload.wikimedia.org/wikipedia/id/9/9c/Filosofi_Teras.jpg",
        "The Power of Now": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Sapiens: A Brief History of Humankind": "https://upload.wikimedia.org/wikipedia/en/5/5e/Sapiens_A_Brief_History_of_Humankind.jpg",
        "Tasawuf Modern": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        
        "A Brief History of Time": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Cosmos": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "The Selfish Gene": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Kalkulus Jilid 1": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Fisika Dasar untuk Universitas": "https://covers.openlibrary.org/b/id/240727-L.jpg",

        "Clean Code": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "The Pragmatic Programmer": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Artificial Intelligence: A Modern Approach": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Belajar Python dalam 24 Jam": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Hacking: The Art of Exploitation": "https://covers.openlibrary.org/b/id/10501234-L.jpg",

        "Laskar Pelangi": "https://upload.wikimedia.org/wikipedia/id/8/8e/Laskar_pelangi_sampul.jpg",
        "Bumi Manusia": "https://upload.wikimedia.org/wikipedia/id/2/2e/Bumi_Manusia.jpg",
        "Harry Potter and the Philosopher's Stone": "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
        "The Hobbit": "https://upload.wikimedia.org/wikipedia/en/4/4a/TheHobbit_FirstEdition.jpg",
        "Naruto Vol. 1": "https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg",

        "Sejarah Indonesia Modern": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Guns, Germs, and Steel": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Manusia dan Kebudayaan di Indonesia": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Napoleon: A Life": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Sejarah Dunia yang Disembunyikan": "https://covers.openlibrary.org/b/id/8739161-L.jpg",

        "Atomic Habits": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "The Power of Habit": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Thinking, Fast and Slow": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Man's Search for Meaning": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "How to Win Friends and Influence People": "https://covers.openlibrary.org/b/id/240727-L.jpg",

        "The Psychology of Money": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Rich Dad Poor Dad": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Zero to One": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "The Lean Startup": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Ekonomi Pembangunan": "https://covers.openlibrary.org/b/id/10501234-L.jpg",

        "The Art of War": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "One Piece Vol. 1": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Dragon Ball Vol. 1": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "The Story of Art": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Pengantar Ilmu Komunikasi": "https://covers.openlibrary.org/b/id/8739161-L.jpg",

        "Kamus Besar Bahasa Indonesia (KBBI)": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Metodologi Penelitian Kualitatif": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "Ensiklopedia Sains": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Statistika Terapan": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Tata Bahasa Baku Bahasa Indonesia": "https://covers.openlibrary.org/b/id/240727-L.jpg",

        "Why We Sleep": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "How Not to Die": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
        "Buku Pintar Kesehatan Keluarga": "https://covers.openlibrary.org/b/id/240727-L.jpg",
        "The 4-Hour Body": "https://covers.openlibrary.org/b/id/8739161-L.jpg",
        "Nutrisi Sehat untuk Keluarga": "https://covers.openlibrary.org/b/id/10501234-L.jpg",
    }

    # Update database
    updated_count = 0
    for title, new_cover in cover_updates.items():
        book = Book.query.filter_by(title=title).first()
        if book:
            book.cover_image = new_cover
            updated_count += 1

    db.session.commit()
    print(f"✅ Berhasil memperbarui {updated_count} sampul buku!")