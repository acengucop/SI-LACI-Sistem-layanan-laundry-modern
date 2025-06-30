from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('pelanggan', 'Pelanggan'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Layanan(models.Model):
    nama = models.CharField(max_length=100)
    harga_per_kg = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nama

class Order(models.Model):
    STATUS = [
        ('diterima', 'Diterima'),
        ('dicuci', 'Dicuci'),
        ('selesai', 'Selesai'),
        ('diambil', 'Diambil'),
    ]
    pelanggan = models.ForeignKey(User, on_delete=models.CASCADE)
    layanan = models.ForeignKey(Layanan, on_delete=models.SET_NULL, null=True)
    berat_kg = models.FloatField()
    jadwal_jemput = models.DateTimeField()
    status_cucian = models.CharField(max_length=20, choices=STATUS, default='diterima')
    tanggal_order = models.DateTimeField(auto_now_add=True)

class Pembayaran(models.Model):
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    bukti_bayar = models.ImageField(upload_to='bukti_bayar/')
    status_bayar = models.BooleanField(default=False)
    tanggal_upload = models.DateTimeField(auto_now_add=True)

class QRIS(models.Model):
    gambar_qris = models.ImageField(upload_to='qris/')
    aktif = models.BooleanField(default=True)
