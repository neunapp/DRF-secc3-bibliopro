from django.contrib import admin

from .models import Autor, Editorial, Libro


admin.site.register(Autor)
admin.site.register(Editorial)
admin.site.register(Libro)
