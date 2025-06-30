from django.contrib import admin
from .models import User, Layanan, Order, Pembayaran, QRIS

admin.site.register(User)
admin.site.register(Layanan)
admin.site.register(Order)
admin.site.register(Pembayaran)
admin.site.register(QRIS)
