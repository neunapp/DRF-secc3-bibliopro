from django.urls import path

from . import views

app_name = "prestamo_app"

urlpatterns = [
    path('api/prestamo/list-fecha',  views.ListarPrestamos.as_view())
]
  