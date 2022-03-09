from django.contrib.auth.models import User, AbstractUser
from django.db import models


class Note(models.Model):
    # Модель заметки
    user = models.ForeignKey(
        'NoteUser',
        on_delete=models.CASCADE,
        related_name='note',
        verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время публикации')

    class Meta:
        ordering = ['-published_at']


class NoteUser(AbstractUser):
    # Модель пользователя
    email = models.EmailField(max_length=255, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
