import sqlite3
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
DATABASE = 'database.db'

def get_db():
    """Fungsi untuk mengoneksikan ke database SQLite."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Fungsi untuk membuat tabel jika belum ada (skema baru dengan kategori)."""
    if not os.path.exists(DATABASE):
        conn = get_db()
        # Membuat tabel dengan kolom category sesuai kebutuhan UI baru
        conn.execute('''
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                description TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()
        print("Database initialized successfully.")

# Jalankan inisialisasi database saat aplikasi dimulai
init_db()

@app.route('/')
def index():
    """Halaman utama untuk menampilkan daftar transaksi."""
    conn = get_db()
    transactions = conn.execute('SELECT * FROM transactions ORDER BY id DESC').fetchall()
    conn.close()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['POST'])
def add_transaction():
    """Fungsi untuk menambahkan transaksi (Pemasukan/Pengeluaran)."""
    description = request.form.get('description')
    amount = request.form.get('amount')
    category = request.form.get('category')

    if description and amount and category:
        try:
            conn = get_db()
            conn.execute(
                'INSERT INTO transactions (description, amount, category) VALUES (?, ?, ?)',
                (description, float(amount), category)
            )
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error saving to database: {e}")

    return redirect(url_for('index'))

if __name__ == '__main__':
    # Host 0.0.0.0 agar bisa diakses dari luar container (Docker)
    app.run(host='0.0.0.0', port=5000, debug=True)