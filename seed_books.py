from app import create_app, db
from app.models import Book

app = create_app()

with app.app_context():
    # HAPUS SEMUA BUKU LAMA DULU
    Book.query.delete()
    db.session.commit()
    
    daftar_buku = [
        # 1. AGAMA & SPIRITUAL (5)
        {"title": "Al-Qur'an dan Terjemahannya", "author": "Kementerian Agama RI", "category": "Agama & Spiritual", "synopsis": "Terjemahan Al-Qur'an dalam bahasa Indonesia beserta tafsir ringkas untuk memudahkan pemahaman.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 10},
        {"title": "Filosofi Teras", "author": "Henry Manampiring", "category": "Agama & Spiritual", "synopsis": "Pengenalan filsafat Stoa yang relevan dengan kehidupan modern untuk mencapai ketenangan batin.", "cover_image": "https://upload.wikimedia.org/wikipedia/id/9/9c/Filosofi_Teras.jpg", "stock": 6},
        {"title": "The Power of Now", "author": "Eckhart Tolle", "category": "Agama & Spiritual", "synopsis": "Panduan spiritual untuk hidup di masa kini dan melepaskan beban masa lalu serta kecemasan masa depan.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 4},
        {"title": "Sapiens: A Brief History of Humankind", "author": "Yuval Noah Harari", "category": "Agama & Spiritual", "synopsis": "Menelusuri sejarah umat manusia dan bagaimana agama serta kepercayaan membentuk peradaban.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/5/5e/Sapiens_A_Brief_History_of_Humankind.jpg", "stock": 5},
        {"title": "Tasawuf Modern", "author": "Hamka", "category": "Agama & Spiritual", "synopsis": "Karya klasik Buya Hamka tentang kebahagiaan, ketenangan jiwa, dan kedekatan dengan Sang Pencipta.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 3},

        # 2. SAINS & MATEMATIKA (5)
        {"title": "A Brief History of Time", "author": "Stephen Hawking", "category": "Sains & Matematika", "synopsis": "Penjelasan populer tentang asal usul alam semesta, lubang hitam, dan hakikat waktu.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/a/a3/BriefHistoryTime.jpg", "stock": 3},
        {"title": "Cosmos", "author": "Carl Sagan", "category": "Sains & Matematika", "synopsis": "Eksplorasi megah tentang alam semesta, evolusi bintang, dan tempat manusia di dalamnya.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/7/7e/Cosmos_book.jpg", "stock": 4},
        {"title": "The Selfish Gene", "author": "Richard Dawkins", "category": "Sains & Matematika", "synopsis": "Pandangan revolusioner tentang evolusi dari sudut pandang gen sebagai unit dasar seleksi alam.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/9/9a/The_Selfish_Gene.jpg", "stock": 2},
        {"title": "Kalkulus Jilid 1", "author": "Purcell & Varberg", "category": "Sains & Matematika", "synopsis": "Buku teks kalkulus komprehensif untuk mahasiswa sains dan teknik, dilengkapi contoh soal.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 8},
        {"title": "Fisika Dasar untuk Universitas", "author": "Halliday & Resnick", "category": "Sains & Matematika", "synopsis": "Referensi fisika klasik yang membahas mekanika, termodinamika, dan elektromagnetisme.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 7},

        # 3. TEKNOLOGI & KOMPUTER (5)
        {"title": "Clean Code", "author": "Robert C. Martin", "category": "Teknologi & Komputer", "synopsis": "Panduan menulis kode yang bersih, mudah dibaca, dan mudah dipelihara oleh programmer profesional.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/2/2a/Clean_Code.jpg", "stock": 5},
        {"title": "The Pragmatic Programmer", "author": "Andrew Hunt & David Thomas", "category": "Teknologi & Komputer", "synopsis": "Dari programmer pemula menjadi master: tips dan filosofi pengembangan perangkat lunak.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/5/5b/Pragmatic_Programmer.jpg", "stock": 4},
        {"title": "Artificial Intelligence: A Modern Approach", "author": "Stuart Russell & Peter Norvig", "category": "Teknologi & Komputer", "synopsis": "Buku teks paling komprehensif tentang kecerdasan buatan, dari pencarian hingga pembelajaran mesin.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 2},
        {"title": "Belajar Python dalam 24 Jam", "author": "Michael Dawson", "category": "Teknologi & Komputer", "synopsis": "Panduan praktis dan cepat untuk menguasai bahasa pemrograman Python dari nol.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 9},
        {"title": "Hacking: The Art of Exploitation", "author": "Jon Erickson", "category": "Teknologi & Komputer", "synopsis": "Memahami cara kerja eksploitasi sistem dan keamanan siber dari level paling dasar.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 3},

        # 4. FIKSI & NOVEL (5)
        {"title": "Laskar Pelangi", "author": "Andrea Hirata", "category": "Fiksi & Novel", "synopsis": "Kisah inspiratif 10 anak Belitung yang berjuang menempuh pendidikan di tengah keterbatasan.", "cover_image": "https://upload.wikimedia.org/wikipedia/id/8/8e/Laskar_pelangi_sampul.jpg", "stock": 10},
        {"title": "Bumi Manusia", "author": "Pramoedya Ananta Toer", "category": "Fiksi & Novel", "synopsis": "Kisah Minke di akhir era kolonialisme Belanda, sebuah mahakarya sastra Indonesia.", "cover_image": "https://upload.wikimedia.org/wikipedia/id/2/2e/Bumi_Manusia.jpg", "stock": 7},
        {"title": "Harry Potter and the Philosopher's Stone", "author": "J.K. Rowling", "category": "Fiksi & Novel", "synopsis": "Petualangan pertama Harry Potter di sekolah sihir Hogwarts yang mengubah dunianya.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/6/6b/Harry_Potter_and_the_Philosopher%27s_Stone_Book_Cover.jpg", "stock": 12},
        {"title": "The Hobbit", "author": "J.R.R. Tolkien", "category": "Fiksi & Novel", "synopsis": "Perjalanan epik Bilbo Baggins mencari harta karun para kurcaci yang dijaga naga Smaug.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/4/4a/TheHobbit_FirstEdition.jpg", "stock": 6},
        {"title": "Naruto Vol. 1", "author": "Masashi Kishimoto", "category": "Fiksi & Novel", "synopsis": "Awal mula perjalanan ninja muda Naruto Uzumaki menuju impiannya menjadi Hokage.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/9/94/NarutoCoverTankobon1.jpg", "stock": 8},

        # 5. SEJARAH & BUDAYA (5)
        {"title": "Sejarah Indonesia Modern", "author": "M.C. Ricklefs", "category": "Sejarah & Budaya", "synopsis": "Sejarah Indonesia sejak abad ke-13 hingga era reformasi, ditulis secara komprehensif.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 5},
        {"title": "Guns, Germs, and Steel", "author": "Jared Diamond", "category": "Sejarah & Budaya", "synopsis": "Mengapa peradaban manusia berkembang tidak merata di seluruh dunia? Sebuah analisis sejarah.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/b/b2/Guns_Germs_and_Steel.jpg", "stock": 4},
        {"title": "Manusia dan Kebudayaan di Indonesia", "author": "Koentjaraningrat", "category": "Sejarah & Budaya", "synopsis": "Studi antropologi mendalam tentang keragaman budaya dan masyarakat di Nusantara.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 3},
        {"title": "Napoleon: A Life", "author": "Andrew Roberts", "category": "Sejarah & Budaya", "synopsis": "Biografi lengkap Napoleon Bonaparte, dari seorang perwira artileri hingga menjadi Kaisar Prancis.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 2},
        {"title": "Sejarah Dunia yang Disembunyikan", "author": "Baharudin A. Rahman", "category": "Sejarah & Budaya", "synopsis": "Mengungkap fakta-fakta sejarah dunia yang jarang dibahas dalam buku pelajaran sekolah.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 4},

        # 6. SELF-IMPROVEMENT & PSIKOLOGI (5)
        {"title": "Atomic Habits", "author": "James Clear", "category": "Self-Improvement & Psikologi", "synopsis": "Cara mudah dan terbukti untuk membangun kebiasaan baik dan menghilangkan kebiasaan buruk.", "cover_image": "https://upload.wikimedia.org/wikipedia/en/9/9e/Atomic_Habits.jpg", "stock": 10},
        {"title": "The Power of Habit", "author": "Charles Duhigg", "category": "Self-Improvement & Psikologi", "synopsis": "Mengapa kebiasaan ada dan bagaimana kita bisa mengubahnya untuk kehidupan yang lebih baik.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 6},
        {"title": "Thinking, Fast and Slow", "author": "Daniel Kahneman", "category": "Self-Improvement & Psikologi", "synopsis": "Menjelajahi dua sistem berpikir manusia: yang cepat dan intuitif vs yang lambat dan analitis.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 5},
        {"title": "Man's Search for Meaning", "author": "Viktor E. Frankl", "category": "Self-Improvement & Psikologi", "synopsis": "Kisah psikiater yang selamat dari kamp Nazi dan menemukan makna hidup dalam penderitaan.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 4},
        {"title": "How to Win Friends and Influence People", "author": "Dale Carnegie", "category": "Self-Improvement & Psikologi", "synopsis": "Buku klasik tentang keterampilan sosial, komunikasi, dan membangun hubungan yang baik.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 7},

        # 7. EKONOMI & BISNIS (5)
        {"title": "The Psychology of Money", "author": "Morgan Housel", "category": "Ekonomi & Bisnis", "synopsis": "Pelajari cara berpikir tentang uang dan bagaimana sikap mental mempengaruhi kesuksesan finansial.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 8},
        {"title": "Rich Dad Poor Dad", "author": "Robert T. Kiyosaki", "category": "Ekonomi & Bisnis", "synopsis": "Pelajaran tentang literasi finansial dan cara membangun aset untuk kebebasan finansial.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 9},
        {"title": "Zero to One", "author": "Peter Thiel", "category": "Ekonomi & Bisnis", "synopsis": "Catatan tentang startup, bagaimana membangun masa depan, dan menciptakan sesuatu yang baru.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 3},
        {"title": "The Lean Startup", "author": "Eric Ries", "category": "Ekonomi & Bisnis", "synopsis": "Metodologi pengembangan bisnis yang mengutamakan iterasi cepat dan umpan balik pelanggan.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 4},
        {"title": "Ekonomi Pembangunan", "author": "Sadono Sukirno", "category": "Ekonomi & Bisnis", "synopsis": "Buku referensi ekonomi yang membahas teori dan kebijakan pembangunan di negara berkembang.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 2},

        # 8. SENI & HIBURAN (5)
        {"title": "The Art of War", "author": "Sun Tzu", "category": "Seni & Hiburan", "synopsis": "Strategi perang kuno yang tetap relevan hingga kini, dapat diterapkan dalam bisnis dan kehidupan.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 5},
        {"title": "One Piece Vol. 1", "author": "Eiichiro Oda", "category": "Seni & Hiburan", "synopsis": "Awal petualangan Monkey D. Luffy mencari harta karun One Piece dan menjadi Raja Bajak Laut.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 10},
        {"title": "Dragon Ball Vol. 1", "author": "Akira Toriyama", "category": "Seni & Hiburan", "synopsis": "Kisah Goku kecil yang mencari bola naga legendaris dan bertemu banyak teman serta musuh kuat.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 8},
        {"title": "The Story of Art", "author": "E.H. Gombrich", "category": "Seni & Hiburan", "synopsis": "Panduan klasik dan mudah dipahami tentang sejarah seni dari zaman purba hingga modern.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 3},
        {"title": "Pengantar Ilmu Komunikasi", "author": "Hafied Cangara", "category": "Seni & Hiburan", "synopsis": "Buku teks dasar-dasar komunikasi, media, dan retorika untuk mahasiswa dan praktisi.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 4},

        # 9. PENDIDIKAN & REFERENSI (5)
        {"title": "Kamus Besar Bahasa Indonesia (KBBI)", "author": "Badan Bahasa", "category": "Pendidikan & Referensi", "synopsis": "Kamus resmi bahasa Indonesia yang menjadi rujukan utama penggunaan kata dan ejaan yang benar.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 5},
        {"title": "Metodologi Penelitian Kualitatif", "author": "Prof. Dr. Sugiyono", "category": "Pendidikan & Referensi", "synopsis": "Panduan lengkap dan praktis untuk mahasiswa dalam melakukan penelitian kualitatif.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 6},
        {"title": "Ensiklopedia Sains", "author": "Tim Penulis", "category": "Pendidikan & Referensi", "synopsis": "Kumpulan pengetahuan sains dasar yang disajikan dengan gambar dan penjelasan yang mudah dimengerti.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 3},
        {"title": "Statistika Terapan", "author": "Prof. Dr. Sudjana", "category": "Pendidikan & Referensi", "synopsis": "Buku teks statistika yang membahas teori dan aplikasi dalam penelitian sosial dan eksakta.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 4},
        {"title": "Tata Bahasa Baku Bahasa Indonesia", "author": "Hasan Alwi", "category": "Pendidikan & Referensi", "synopsis": "Panduan resmi tata bahasa Indonesia untuk penulisan yang baik dan benar.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 2},

        # 10. KESEHATAN & GAYA HIDUP (5)
        {"title": "Why We Sleep", "author": "Matthew Walker", "category": "Kesehatan & Gaya Hidup", "synopsis": "Mengungkap kekuatan dan manfaat tidur untuk kesehatan otak dan tubuh manusia.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 5},
        {"title": "How Not to Die", "author": "Michael Greger", "category": "Kesehatan & Gaya Hidup", "synopsis": "Panduan nutrisi berbasis ilmiah untuk mencegah dan mengobati penyakit dengan pola makan.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 4},
        {"title": "Buku Pintar Kesehatan Keluarga", "author": "Dr. Andi Putra", "category": "Kesehatan & Gaya Hidup", "synopsis": "Panduan praktis pertolongan pertama dan perawatan kesehatan sehari-hari untuk seluruh keluarga.", "cover_image": "https://covers.openlibrary.org/b/id/8739161-L.jpg", "stock": 7},
        {"title": "The 4-Hour Body", "author": "Timothy Ferriss", "category": "Kesehatan & Gaya Hidup", "synopsis": "Eksperimen rahasia untuk menurunkan berat badan, meningkatkan performa, dan hidup lebih sehat.", "cover_image": "https://covers.openlibrary.org/b/id/10501234-L.jpg", "stock": 3},
        {"title": "Nutrisi Sehat untuk Keluarga", "author": "Dian Puspita", "category": "Kesehatan & Gaya Hidup", "synopsis": "Panduan menyusun menu sehat dan bergizi seimbang untuk keluarga dengan bahan lokal.", "cover_image": "https://covers.openlibrary.org/b/id/240727-L.jpg", "stock": 5},
    ]

    count = 0
    for b in daftar_buku:
        buku_baru = Book(**b)
        db.session.add(buku_baru)
        count += 1

    db.session.commit()
    print(f"✅ BERHASIL! {count} buku dengan sampul baru telah dimasukkan ke database.")