from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Order, Pembayaran

# Tailwind-friendly CSS for input styling
INPUT_CLASS = 'w-full px-4 py-3 rounded-lg border border-blue-300 bg-white focus:ring-2 focus:ring-blue-400 focus:outline-none transition duration-300 ease-in-out shadow-sm hover:shadow-md'

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'role', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Email'}),
            'role': forms.Select(attrs={'class': INPUT_CLASS}),
            'password1': forms.PasswordInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Konfirmasi Password'}),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['layanan', 'berat_kg', 'jadwal_jemput']
        widgets = {
            'layanan': forms.Select(attrs={'class': INPUT_CLASS}),
            'berat_kg': forms.NumberInput(attrs={'class': INPUT_CLASS, 'placeholder': 'Berat cucian (kg)'}),
            'jadwal_jemput': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': INPUT_CLASS
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['jadwal_jemput'].input_formats = ['%Y-%m-%dT%H:%M']


class PembayaranForm(forms.ModelForm):
    class Meta:
        model = Pembayaran
        fields = ['bukti_bayar']
        widgets = {
            'bukti_bayar': forms.ClearableFileInput(attrs={'class': INPUT_CLASS}),
        }
