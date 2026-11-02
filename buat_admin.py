from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    # Cek apakah admin sudah ada
    admin = User.query.filter_by(username='admin').first()
    
    if admin:
        # Kalau sudah ada, kita reset passwordnya
        admin.set_password('admin123')
        db.session.commit()
        print("✅ Akun 'admin' sudah ada. Password berhasil di-reset menjadi 'admin123'!")
    else:
        # Kalau belum ada, kita bikin baru
        new_admin = User(username='admin', email='admin@perpus.com', role='admin')
        new_admin.set_password('admin123')
        db.session.add(new_admin)
        db.session.commit()
        print("✅ Akun 'admin' berhasil dibuat dengan password 'admin123'!")