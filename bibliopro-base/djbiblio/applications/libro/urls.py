from django.urls import path

from . import views

app_name = "libro_app"

urlpatterns = [
    path('api/autor/list',  views.ListaAutores.as_view())
]
    
    
    
    
    
    
    
    