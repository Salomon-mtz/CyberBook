from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Usuarios


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    username = forms.CharField(max_length=100)
    password1 = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=100)
    escuela = forms.CharField(max_length=100)
    rol = forms.CharField(max_length=100)
    
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "telefono", "escuela", "rol")

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(max_length=100,required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    class Meta:
        model = Usuarios
        fields = ('username', 'password', 'rol', 'school', 'phone')



