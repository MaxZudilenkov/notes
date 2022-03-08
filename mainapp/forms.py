from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from mainapp.models import NoteUser, Note


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

    def clean_email(self):
        email = self.cleaned_data['email']
        user = NoteUser.objects.filter(email__iexact=email)
        if user:
            raise forms.ValidationError('Такой адрес электронной потчы уже зарегистрирован')
        return email.lower()


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(label='Пароль')

    error_messages = {
        'invalid_login': (
            "Ошибка в адресе электронной почты или пароле"

        ),

    }


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text', 'user')
        widgets = {'user': forms.HiddenInput(), }

    def clean(self):
        data = self.cleaned_data
        if len(data['text']) == 0:
            raise forms.ValidationError('Вы не можете добавить пустую заметку')
        return data
