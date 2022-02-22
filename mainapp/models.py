from django.contrib.auth.models import User
from django.db import models


class Note(models.Model):
    # Модель заметки
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='note', verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время публикации')
