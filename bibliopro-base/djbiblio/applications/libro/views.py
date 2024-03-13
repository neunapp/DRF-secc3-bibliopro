from django.shortcuts import render

from rest_framework.generics import ListAPIView

#
from .models import Autor
from .serializers import AutorSerializer


class ListaAutores(ListAPIView):
    serializer_class = AutorSerializer
    
    def get_queryset(self):
        queryset = Autor.objects.listar_autores_pais('Argentina')
        return queryset
