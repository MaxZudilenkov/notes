from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта')
    password1 = forms.CharField(label='Введите пароль')
    password2 = forms.CharField(label='Повторите пароль')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')

    error_messages = {
        'password_mismatch': ('Введенные пароли не совпадают'),
    }
