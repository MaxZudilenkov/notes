from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mainapp.forms import RegisterUserForm, UserLoginForm
from mainapp.models import NoteUser


class RegisterUserView(CreateView):
    # Класс для регистрации пользователей
    model = NoteUser
    template_name = 'mainapp/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')


class UserLoginView(LoginView):
    # Класс для авторизации пользователей
    authentication_form = UserLoginForm
    template_name = 'mainapp/login.html'
    success_url = reverse_lazy('main')


def user_logout(request):
    # Метод для выхода из системы
    logout(request)
    return redirect('main')


def show_main_page(request):
    return render(request, 'mainapp/main.html')
