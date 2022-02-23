from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

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


class UserLoginForm(AuthenticationForm):
    password = forms.CharField(label='Пароль')


class AddNoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('text', 'user')

    def clean(self):
        data = self.cleaned_data
        if len(data['text']) == 0:
            raise forms.ValidationError('Вы не можете сохранить пустую заметку')
        return data
