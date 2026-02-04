# Gunakan image Python yang ringan
FROM python:3.9-slim

# Set direktori kerja di dalam container
WORKDIR /app

# Salin file requirements dan install library
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin seluruh kode aplikasi
COPY . .

# Expose port aplikasi
EXPOSE 5000

# Jalankan aplikasi
CMD ["python", "app.py"]