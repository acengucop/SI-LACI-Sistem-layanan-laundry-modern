from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Order, Layanan, Pembayaran, QRIS
from .forms import OrderForm, PembayaranForm, CustomUserCreationForm


# ================================
# HALAMAN UMUM
# ================================
def home_view(request):
    return render(request, 'silaci/home.html')


# ================================
# AUTENTIKASI
# ================================
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'silaci/register.html', {'form': form})


def login_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            context['error'] = 'Username atau password salah'
    return render(request, 'silaci/login.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')


# ================================
# HALAMAN UTAMA LOGIN
# ================================
@login_required
def dashboard_view(request):
    if request.user.role == 'admin':
        orders = Order.objects.all()
    else:
        orders = Order.objects.filter(pelanggan=request.user)
    return render(request, 'silaci/dashboard.html', {'orders': orders})


# ================================
# ORDER & PEMBAYARAN
# ================================
@login_required
def buat_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.pelanggan = request.user
            order.save()
            return redirect('upload_bukti', order.id)
    else:
        form = OrderForm()
    return render(request, 'silaci/buat_order.html', {'form': form})


@login_required
def upload_bukti_view(request, order_id):
    order = get_object_or_404(Order, id=order_id, pelanggan=request.user)
    if request.method == 'POST':
        form = PembayaranForm(request.POST, request.FILES)
        if form.is_valid():
            pembayaran = form.save(commit=False)
            pembayaran.order = order
            pembayaran.save()
            return redirect('dashboard')
    else:
        form = PembayaranForm()

    qris = QRIS.objects.filter(aktif=True).first()
    return render(request, 'silaci/upload_bukti.html', {'form': form, 'qris': qris})
