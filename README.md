# SI-LACI - Sistem Layanan Laundry Modern

Sistem layanan laundry modern berbasis web menggunakan Django. Aplikasi ini memudahkan pelanggan untuk melakukan pemesanan, pelacakan status cucian, serta mengunggah bukti pembayaran melalui QRIS. SI-LACI juga menyediakan dashboard untuk admin dalam mengelola layanan, harga, dan laporan transaksi.

---

## 🚀 Fitur Utama

- Registrasi & Login pelanggan dan admin
- Pemesanan layanan laundry (cuci, setrika, dll)
- Penjadwalan antar/jemput cucian dengan kalender
- Upload bukti pembayaran berbasis gambar (QRIS)
- Pelacakan status cucian
- Dashboard pelanggan & admin
- Panel admin bawaan Django

---

## 🛠️ Teknologi yang Digunakan

- Python 3.x
- Django 5.2
- SQLite (default DB untuk dev)
- Pillow (untuk upload gambar)
- HTML5 (form kalender `datetime-local`)
- CSS inline (bisa upgrade ke Bootstrap/Tailwind)
- Git & GitHub

---

## 💻 Cara Setup Proyek di Lokal

### 1. Clone Repository
```bash
git clone https://github.com/acengucop/SI-LACI-Sistem-layanan-laundry-modern.git
cd SI-LACI-Sistem-layanan-laundry-modern

2. Buat Virtual Environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/macOS

pip install django pillow


