from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, timedelta
from functools import wraps

from app import db
from app.models import User, Book, Loan, Bookmark
from app.services import search_books_api

main = Blueprint("main", __name__)

# --- DEKORATOR KEAMANAN ADMIN ---
def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash("Akses ditolak! Halaman ini hanya untuk Admin.", "danger")
            return redirect(url_for('main.index'))
        return f(*args, **kwargs)
    return decorated_function

# --- HALAMAN UTAMA ---
@main.route("/")
def index():
    books = Book.query.order_by(Book.created_at.desc()).limit(12).all()
    return render_template("index.html", books=books)

# --- HALAMAN DETAIL BUKU ---
@main.route("/book/<int:book_id>")
def book_detail(book_id):
    book = Book.query.get_or_404(book_id)
    is_bookmarked = False
    if current_user.is_authenticated:
        is_bookmarked = Bookmark.query.filter_by(user_id=current_user.id, book_id=book.id).first() is not None
    return render_template("book_detail.html", book=book, is_bookmarked=is_bookmarked)

# --- KATALOG (DENGAN 10 KATEGORI RESMI) ---
@main.route("/catalog")
def catalog():
    q = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip()
    books = []
    
    # Daftar 10 Kategori Resmi
    DAFTAR_KATEGORI = [
        "Agama & Spiritual",
        "Sains & Matematika",
        "Teknologi & Komputer",
        "Fiksi & Novel",
        "Sejarah & Budaya",
        "Self-Improvement & Psikologi",
        "Ekonomi & Bisnis",
        "Seni & Hiburan",
        "Pendidikan & Referensi",
        "Kesehatan & Gaya Hidup"
    ]
    
    if q:
        books = search_books_api(q)
    else:
        query = Book.query
        if category:
            query = query.filter(Book.category == category)
        books = query.order_by(Book.title.asc()).all()
        
    return render_template("catalog.html", books=books, categories=DAFTAR_KATEGORI, q=q, category=category)

# --- SIMPAN BUKU DARI API ---
@main.route("/catalog/save", methods=["POST"])
@login_required
def save_external_book():
    title = request.form.get("title")
    author = request.form.get("author")
    category = request.form.get("category")
    synopsis = request.form.get("synopsis")
    cover_image = request.form.get("cover_image")
    
    existing_book = Book.query.filter_by(title=title).first()
    if existing_book:
        flash(f"Buku '{title}' sudah ada di perpustakaan lokal.", "warning")
        return redirect(url_for("main.catalog"))
    
    new_book = Book(title=title, author=author, category=category, synopsis=synopsis, cover_image=cover_image, stock=1)
    db.session.add(new_book)
    db.session.commit()
    flash(f"Berhasil menyimpan '{title}' ke katalog lokal!", "success")
    return redirect(url_for("main.catalog"))

# --- FITUR BOOKMARK ---
@main.route("/bookmark")
@login_required
def my_bookmarks():
    bookmarks = Bookmark.query.filter_by(user_id=current_user.id).order_by(Bookmark.created_at.desc()).all()
    return render_template("bookmark.html", bookmarks=bookmarks)

@main.route("/bookmark/add/<int:book_id>", methods=["POST"])
@login_required
def add_bookmark(book_id):
    book = Book.query.get_or_404(book_id)
    existing = Bookmark.query.filter_by(user_id=current_user.id, book_id=book.id).first()
    if existing:
        flash("Buku ini sudah ada di Bookmark Anda.", "warning")
    else:
        new_bookmark = Bookmark(user_id=current_user.id, book_id=book.id)
        db.session.add(new_bookmark)
        db.session.commit()
        flash(f"'{book.title}' berhasil ditambahkan ke Bookmark!", "success")
    return redirect(request.referrer or url_for("main.catalog"))

@main.route("/bookmark/remove/<int:bookmark_id>", methods=["POST"])
@login_required
def remove_bookmark(bookmark_id):
    bookmark = Bookmark.query.get_or_404(bookmark_id)
    if bookmark.user_id == current_user.id:
        db.session.delete(bookmark)
        db.session.commit()
        flash("Buku dihapus dari Bookmark.", "info")
    return redirect(url_for("main.my_bookmarks"))

# --- PROFIL & PENGATURAN AKUN ---
@main.route("/profile")
@login_required
def profile():
    active_loans = Loan.query.filter_by(user_id=current_user.id, status="borrowed").count()
    history_loans = Loan.query.filter_by(user_id=current_user.id, status="returned").count()
    total_bookmarks = Bookmark.query.filter_by(user_id=current_user.id).count()
    return render_template("profile.html", active_loans=active_loans, history_loans=history_loans, total_bookmarks=total_bookmarks)

@main.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    if request.method == "POST":
        old_password = request.form.get("old_password")
        new_password = request.form.get("new_password")
        confirm_password = request.form.get("confirm_password")

        if not current_user.check_password(old_password):
            flash("Password lama salah!", "danger")
        elif new_password != confirm_password:
            flash("Password baru dan konfirmasi tidak cocok!", "danger")
        elif len(new_password) < 4:
            flash("Password baru terlalu pendek (minimal 4 karakter).", "danger")
        else:
            current_user.set_password(new_password)
            db.session.commit()
            flash("Password berhasil diubah!", "success")
            return redirect(url_for("main.profile"))
    return render_template("change_password.html")

# --- REGISTRASI & LOGIN ---
@main.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        user_exists = User.query.filter((User.username == username) | (User.email == email)).first()
        if user_exists:
            flash("Username atau Email sudah terdaftar.", "danger")
            return redirect(url_for("main.register"))
        new_user = User(username=username, email=email, role="member")
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash("Pendaftaran berhasil! Silakan masuk.", "success")
        return redirect(url_for("main.login"))
    return render_template("register.html")

@main.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            login_user(user)
            flash(f"Selamat datang, {user.username}!", "success")
            return redirect(url_for("main.index"))
        flash("Username atau password salah.", "danger")
    return render_template("login.html")

@main.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Anda telah keluar.", "info")
    return redirect(url_for("main.index"))

# --- FITUR PINJAM & KEMBALI ---
@main.route("/borrow/<int:book_id>", methods=["POST"])
@login_required
def borrow(book_id):
    book = Book.query.get_or_404(book_id)
    if book.stock <= 0:
        flash("Maaf, stok buku habis.", "danger")
        return redirect(url_for("main.book_detail", book_id=book.id))
    existing_loan = Loan.query.filter_by(user_id=current_user.id, book_id=book.id, status="borrowed").first()
    if existing_loan:
        flash("Anda masih meminjam buku ini.", "danger")
        return redirect(url_for("main.book_detail", book_id=book.id))
    due_date = datetime.utcnow() + timedelta(days=7)
    new_loan = Loan(user_id=current_user.id, book_id=book.id, due_date=due_date)
    book.stock -= 1
    db.session.add(new_loan)
    db.session.commit()
    flash(f"Berhasil meminjam '{book.title}'.", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/return/<int:loan_id>", methods=["POST"])
@login_required
def return_book(loan_id):
    loan = Loan.query.get_or_404(loan_id)
    if current_user.role != "admin" and current_user.id != loan.user_id:
        flash("Anda tidak berhak.", "danger")
        return redirect(url_for("main.index"))
    if loan.status == "returned":
        flash("Buku sudah dikembalikan.", "warning")
        return redirect(url_for("main.dashboard"))
    now = datetime.utcnow()
    fine = 0
    if now > loan.due_date:
        late_days = (now - loan.due_date).days
        fine = late_days * 2000
    loan.return_date = now
    loan.fine_amount = fine
    loan.status = "returned"
    loan.book.stock += 1
    db.session.commit()
    if fine > 0:
        flash(f"Terlambat! Denda: Rp {fine:,}".replace(",", "."), "danger")
    else:
        flash("Dikembalikan tepat waktu. Terima kasih!", "success")
    return redirect(url_for("main.dashboard"))

@main.route("/dashboard")
@login_required
def dashboard():
    active_loans = Loan.query.filter_by(user_id=current_user.id, status="borrowed").all()
    history_loans = Loan.query.filter_by(user_id=current_user.id, status="returned").order_by(Loan.return_date.desc()).all()
    return render_template("dashboard.html", active_loans=active_loans, history_loans=history_loans)

# --- AREA ADMIN ---
@main.route("/admin")
@login_required
@admin_required
def admin_dashboard():
    total_books = Book.query.count()
    total_stock = db.session.query(db.func.sum(Book.stock)).scalar() or 0
    members = User.query.filter_by(role="member").all()
    all_loans = Loan.query.order_by(Loan.borrow_date.desc()).all()
    return render_template("admin.html", total_books=total_books, total_stock=total_stock, members=members, all_loans=all_loans, books=Book.query.all())

@main.route("/admin/book/add", methods=["GET", "POST"])
@login_required
@admin_required
def add_book():
    DAFTAR_KATEGORI = [
        "Agama & Spiritual", "Sains & Matematika", "Teknologi & Komputer", 
        "Fiksi & Novel", "Sejarah & Budaya", "Self-Improvement & Psikologi", 
        "Ekonomi & Bisnis", "Seni & Hiburan", "Pendidikan & Referensi", "Kesehatan & Gaya Hidup"
    ]
    if request.method == "POST":
        title = request.form.get("title")
        author = request.form.get("author")
        category = request.form.get("category")
        synopsis = request.form.get("synopsis")
        stock = int(request.form.get("stock", 1))
        cover_image = request.form.get("cover_image")
        new_book = Book(title=title, author=author, category=category, synopsis=synopsis, stock=stock, cover_image=cover_image)
        db.session.add(new_book)
        db.session.commit()
        flash("Buku baru berhasil ditambahkan!", "success")
        return redirect(url_for("main.admin_dashboard"))
    return render_template("book_form.html", action="Tambah", book=None, categories=DAFTAR_KATEGORI)

@main.route("/admin/book/edit/<int:book_id>", methods=["GET", "POST"])
@login_required
@admin_required
def edit_book(book_id):
    DAFTAR_KATEGORI = [
        "Agama & Spiritual", "Sains & Matematika", "Teknologi & Komputer", 
        "Fiksi & Novel", "Sejarah & Budaya", "Self-Improvement & Psikologi", 
        "Ekonomi & Bisnis", "Seni & Hiburan", "Pendidikan & Referensi", "Kesehatan & Gaya Hidup"
    ]
    book = Book.query.get_or_404(book_id)
    if request.method == "POST":
        book.title = request.form.get("title")
        book.author = request.form.get("author")
        book.category = request.form.get("category")
        book.synopsis = request.form.get("synopsis")
        book.stock = int(request.form.get("stock", 1))
        book.cover_image = request.form.get("cover_image")
        db.session.commit()
        flash("Data buku berhasil diperbarui!", "success")
        return redirect(url_for("main.admin_dashboard"))
    return render_template("book_form.html", action="Edit", book=book, categories=DAFTAR_KATEGORI)

@main.route("/admin/book/delete/<int:book_id>", methods=["POST"])
@login_required
@admin_required
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    active_loan = Loan.query.filter_by(book_id=book.id, status="borrowed").first()
    if active_loan:
        flash("Gagal menghapus! Buku ini sedang dipinjam.", "danger")
    else:
        db.session.delete(book)
        db.session.commit()
        flash("Buku berhasil dihapus dari database.", "info")
    return redirect(url_for("main.admin_dashboard"))