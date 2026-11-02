from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # Kita gunakan link Google Books berdasarkan ISBN / ID Buku yang valid
    # Format: https://books.google.com/books/content?id=ID_BUKU&printsec=frontcover&img=1&zoom=1
    
    gambar_asli = {
        "Al-Qur'an dan Terjemahannya": "https://books.google.com/books/content?id=fDg0EAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Filosofi Teras": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "The Power of Now": "https://books.google.com/books/content?id=1T0hAQAAIAAJ&printsec=frontcover&img=1&zoom=1",
        "Sapiens: A Brief History of Humankind": "https://books.google.com/books/content?id=FmyBAgAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Tasawuf Modern": "https://books.google.com/books/content?id=2g5CDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        
        "A Brief History of Time": "https://books.google.com/books/content?id=oZhqDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Cosmos": "https://books.google.com/books/content?id=Y2w_AQAAIAAJ&printsec=frontcover&img=1&zoom=1",
        "The Selfish Gene": "https://books.google.com/books/content?id=3Xw7DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Kalkulus Jilid 1": "https://books.google.com/books/content?id=8g0dAAAAMAAJ&printsec=frontcover&img=1&zoom=1",
        "Fisika Dasar untuk Universitas": "https://books.google.com/books/content?id=1l0aAQAAMAAJ&printsec=frontcover&img=1&zoom=1",

        "Clean Code": "https://books.google.com/books/content?id=_i6bDeoCQzsC&printsec=frontcover&img=1&zoom=1",
        "The Pragmatic Programmer": "https://books.google.com/books/content?id=5wBQEp6ruIAC&printsec=frontcover&img=1&zoom=1",
        "Artificial Intelligence: A Modern Approach": "https://books.google.com/books/content?id=8jZBksh-bUMC&printsec=frontcover&img=1&zoom=1",
        "Belajar Python dalam 24 Jam": "https://books.google.com/books/content?id=v4QjAQAAMAAJ&printsec=frontcover&img=1&zoom=1",
        "Hacking: The Art of Exploitation": "https://books.google.com/books/content?id=4l9LAAAAMAAJ&printsec=frontcover&img=1&zoom=1",

        "Laskar Pelangi": "https://upload.wikimedia.org/wikipedia/id/8/8e/Laskar_pelangi_sampul.jpg",
        "Bumi Manusia": "https://upload.wikimedia.org/wikipedia/id/2/2e/Bumi_Manusia.jpg",
        "Harry Potter and the Philosopher's Stone": "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg",
        "The Hobbit": "https://upload.wikimedia.org/wikipedia/en/4/4a/TheHobbit_FirstEdition.jpg",
        "Naruto Vol. 1": "https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg",

        "Sejarah Indonesia Modern": "https://books.google.com/books/content?id=4fYpAQAAMAAJ&printsec=frontcover&img=1&zoom=1",
        "Guns, Germs, and Steel": "https://books.google.com/books/content?id=1Qw3DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Manusia dan Kebudayaan di Indonesia": "https://books.google.com/books/content?id=6xQkAAAAMAAJ&printsec=frontcover&img=1&zoom=1",
        "Napoleon: A Life": "https://books.google.com/books/content?id=0BylBAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Sejarah Dunia yang Disembunyikan": "https://books.google.com/books/content?id=5vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",

        "Atomic Habits": "https://books.google.com/books/content?id=XfFvDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "The Power of Habit": "https://books.google.com/books/content?id=1U7fDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Thinking, Fast and Slow": "https://books.google.com/books/content?id=oV1lDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Man's Search for Meaning": "https://books.google.com/books/content?id=K2ZcDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "How to Win Friends and Influence People": "https://books.google.com/books/content?id=6h-TDwAAQBAJ&printsec=frontcover&img=1&zoom=1",

        "The Psychology of Money": "https://books.google.com/books/content?id=T7YQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Rich Dad Poor Dad": "https://books.google.com/books/content?id=V4wQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Zero to One": "https://books.google.com/books/content?id=8hGvDwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "The Lean Startup": "https://books.google.com/books/content?id=r9xTAAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Ekonomi Pembangunan": "https://books.google.com/books/content?id=8g0dAAAAMAAJ&printsec=frontcover&img=1&zoom=1",

        "The Art of War": "https://books.google.com/books/content?id=Y8s_AAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "One Piece Vol. 1": "https://books.google.com/books/content?id=J3sQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Dragon Ball Vol. 1": "https://books.google.com/books/content?id=Z3sQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "The Story of Art": "https://books.google.com/books/content?id=Z3sQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Pengantar Ilmu Komunikasi": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",

        "Kamus Besar Bahasa Indonesia (KBBI)": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Metodologi Penelitian Kualitatif": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Ensiklopedia Sains": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Statistika Terapan": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Tata Bahasa Baku Bahasa Indonesia": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",

        "Why We Sleep": "https://books.google.com/books/content?id=T7YQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "How Not to Die": "https://books.google.com/books/content?id=Z3sQEAAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Buku Pintar Kesehatan Keluarga": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "The 4-Hour Body": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
        "Nutrisi Sehat untuk Keluarga": "https://books.google.com/books/content?id=6vN1DwAAQBAJ&printsec=frontcover&img=1&zoom=1",
    }

    updated_count = 0
    for title, new_cover in gambar_asli.items():
        book = Book.query.filter_by(title=title).first()
        if book:
            book.cover_image = new_cover
            updated_count += 1

    db.session.commit()
    print(f"✅ Berhasil memperbarui {updated_count} sampul buku dengan gambar asli dari Google Books!")