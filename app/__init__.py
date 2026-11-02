from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Inisialisasi ekstensi di luar fungsi agar bisa di-import oleh file lain
db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    # Konfigurasi dasar aplikasi
    app.config["SECRET_KEY"] = "kunci-rahasia-perpus-modern"
    # Sesuai instruksi: menggunakan SQLite bernama library.db
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Inisialisasi database dan sistem login
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "main.login"
    login_manager.login_message = "Silakan masuk terlebih dahulu."

    # Mendaftarkan blueprint (jika ada)
    from app.routes import main
    app.register_blueprint(main)

    # Membuat tabel database otomatis di dalam konteks aplikasi
    with app.app_context():
        from app import models  # Import model agar dikenali
        db.create_all()

    return app

# Callback untuk memuat user dari database berdasarkan ID (wajib untuk Flask-Login)
@login_manager.user_loader
def load_user(user_id):
    from app.models import User
    return User.query.get(int(user_id))