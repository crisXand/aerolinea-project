from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.db import models
from django import forms
from captcha.fields import CaptchaField

class UsuarioNuevoForm(UserCreationForm):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        self.fields['username'].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuario',max_length=50, required=True)
    password = forms.CharField(label='Clave', max_length=100, required=True,widget=forms.PasswordInput)

class CaptchForm(forms.Form):
    captcha = CaptchaField()
