from django.contrib import admin

from mainapp.models import Note, NoteUser


class NoteAdmin(admin.ModelAdmin):
    list_display = ('user', 'text', 'published_at')


class NoteUserAdmin(admin.ModelAdmin):
    list_display = ('email',)


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteUser, NoteUserAdmin)
