# uas-rpl
# Personal Finance Tracker - UAS Rekayasa Perangkat Lunak Lanjut

Aplikasi pencatatan keuangan pribadi berbasis web yang dikembangkan menggunakan Python Flask, diimplementasikan dengan teknologi Containerization (Docker) dan Pipeline CI/CD otomatis menggunakan GitHub Actions.

## 🚀 Fitur Utama
* **CRUD Transaksi:** Mencatat pemasukan dan pengeluaran secara dinamis.
* **Database SQLite:** Penyimpanan data yang ringan dan efisien.
* **Dockerized:** Terisolasi penuh dalam kontainer untuk konsistensi lingkungan.
* **Automated CI/CD:** Validasi otomatis setiap perubahan kode melalui GitHub Actions.

## 🛠️ Arsitektur Teknologi
* **Language:** [Python 3.9+](https://www.python.org/)
* **Framework:** [Flask](https://flask.palletsprojects.com/)
* **Containerization:** [Docker](https://www.docker.com/)
* **CI/CD Platform:** [GitHub Actions](https://github.com/features/actions)

## 📦 Panduan Instalasi Lokal

### 1. Prasyarat
Pastikan Anda telah menginstal:
* Python 3.x
* Docker Desktop

### 2. Menjalankan Secara Lokal (Tanpa Docker)
```powershell
# Clone repositori
git clone [https://github.com/USERNAME_ANDA/NAMA_REPO.git](https://github.com/USERNAME_ANDA/NAMA_REPO.git)

# Install dependensi
pip install -r requirements.txt

# Jalankan aplikasi
python app.py

#Aplikasi akan berjalan di: http://127.0.0.1:5000

#menjalankan menggunakan docker
# Build Image
docker build -t finance-app:v1 .

# Run Container
docker run -d -p 5000:5000 --name uas-container finance-app:v1

#Aplikasi akan berjalan di: http://localhost:5000