from django.contrib import admin

from .models import Estudiante, Prestamo, Devolucion


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'last_name',
    )


class PrestamoAdmin(admin.ModelAdmin):
    list_display = (
        'book',
        'student',
        'date',
    )

admin.site.register(Prestamo, PrestamoAdmin)

admin.site.register(Devolucion)