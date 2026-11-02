from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

# 1. Model User (dengan inheritance UserMixin)
class User(UserMixin, db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(256), nullable=False)
    # Sesuai instruksi: role (admin/member), default-nya member
    role = db.Column(db.String(20), default="member", nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password: str) -> None:
        self.password_hash = generate_password_hash(password)

    def check_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def __repr__(self) -> str:
        return f"<User {self.username} ({self.role})>"


# 2. Model Book
class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, index=True)
    author = db.Column(db.String(120), nullable=False)
    # Sesuai instruksi: synopsis dan cover_image
    synopsis = db.Column(db.Text, nullable=True)
    cover_image = db.Column(db.String(255), nullable=True) # Menyimpan nama file gambar
    stock = db.Column(db.Integer, default=1)
    category = db.Column(db.String(80), nullable=True, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"<Book {self.title}>"

        # Tambahkan di bagian paling bawah models.py
class Loan(db.Model):
    __tablename__ = "loans"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    borrow_date = db.Column(db.DateTime, default=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=False)
    return_date = db.Column(db.DateTime, nullable=True) # Diisi kalau sudah dikembalikan
    fine_amount = db.Column(db.Integer, default=0) # Denda (Rp)
    status = db.Column(db.String(20), default="borrowed") # "borrowed" atau "returned"

    # Relasi agar kita bisa akses data user dan buku dari transaksi ini
    user = db.relationship('User', backref='loans')
    book = db.relationship('Book', backref='loans')

    def __repr__(self):
        return f"<Loan {self.book.title} by {self.user.username}>"

        # Tambahkan di paling bawah models.py
class Bookmark(db.Model):
    __tablename__ = "bookmarks"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('books.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relasi
    user = db.relationship('User', backref='bookmarks')
    book = db.relationship('Book', backref='bookmarks')

    def __repr__(self):
        return f"<Bookmark {self.book.title} by {self.user.username}>"