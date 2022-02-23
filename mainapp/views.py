from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from mainapp.forms import RegisterUserForm, UserLoginForm, AddNoteForm
from mainapp.models import NoteUser, Note


class RegisterUserView(CreateView):
    # Класс для регистрации пользователей
    model = NoteUser
    template_name = 'mainapp/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        # Метод для автоматического входа после регистрации
        valid_form = super().form_valid(form)
        user = authenticate(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password1'), )
        print(user)
        login(self.request, user)
        return valid_form


class UserLoginView(LoginView):
    # Класс для авторизации пользователей
    authentication_form = UserLoginForm
    template_name = 'mainapp/login.html'
    success_url = reverse_lazy('main')


def user_logout(request):
    # Метод для выхода из системы
    logout(request)
    return redirect('main')


def add_note(request):
    # Метод для добавления заметки
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            if int(request.POST.get('user')) == request.user.pk:
                form.save()
                return redirect('main')
    else:
        form = AddNoteForm(initial={'user': request.user})
    context = {'form': form}
    return render(request, 'mainapp/add_note.html', context)


class NotesListView(ListView):
    # Класс для отображения заметок пользователя
    template_name = 'mainapp/notes_list.html'
    context_object_name = 'notes'

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user.pk)


def show_main_page(request):
    # Метод для отображения главной страницы
    user_id = request.user.pk
    all_user_notes = Note.objects.filter(user=user_id)
    context = {'all_user_notes': all_user_notes}
    return render(request, 'mainapp/main.html', context)
