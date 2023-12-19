from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Libro, Autor, Genero
admin.site.register(Libro)
admin.site.register(Autor)
admin.site.register(Genero)