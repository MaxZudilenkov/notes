from cProfile import label

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from mainapp.models import NoteUser


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(label='Электронная почта')
    password1 = forms.CharField(label='Введите пароль')
    password2 = forms.CharField(label='Повторите пароль')

    class Meta:
        model = NoteUser
        fields = ('email', 'password1', 'password2')

    error_messages = {
        'password_mismatch': ('Введенные пароли не совпадают'),
    }


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(label='Пароль')
