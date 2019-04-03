from django.contrib import admin
from apps.curso.models import Persona, Curso

# Register your models here.

# @admin.register(Persona)
# class ViewAdmin(ImportExportModelAdmin):
#     pass

admin.site.register(Curso)