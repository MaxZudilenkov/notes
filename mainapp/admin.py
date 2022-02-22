from django.contrib import admin

from mainapp.models import Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'published_at')


admin.site.register(Note, NoteAdmin)
