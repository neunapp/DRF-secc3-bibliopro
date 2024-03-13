from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('applications.libro.urls'), name="libro_app"),
    path('', include('applications.prestamo.urls'), name="prestamo_app")
]
