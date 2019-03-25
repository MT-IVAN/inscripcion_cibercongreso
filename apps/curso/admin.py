from django.contrib import admin

from apps.curso.models import Persona, Curso

# Register your models here.

admin.site.register(Persona)
admin.site.register(Curso)