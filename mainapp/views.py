from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from mainapp.forms import RegisterUserForm
from mainapp.models import NoteUser


class RegisterUserView(CreateView):
    # Класс для регистрации пользователей
    model = NoteUser
    template_name = 'mainapp/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')


def show_main_page(request):
    return render(request, 'mainapp/main.html')
