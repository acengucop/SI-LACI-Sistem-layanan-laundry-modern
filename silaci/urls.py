from django.urls import path
from . import views

urlpatterns = [
    # Halaman publik
    path('', views.home_view, name='home'),

    # Autentikasi
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    # Halaman utama setelah login
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # Pemesanan dan pembayaran
    path('order/', views.buat_order_view, name='buat_order'),
    path('order/<int:order_id>/upload/', views.upload_bukti_view, name='upload_bukti'),
]
