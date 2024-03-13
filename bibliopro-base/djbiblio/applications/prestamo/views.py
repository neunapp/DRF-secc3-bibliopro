from django.shortcuts import render

from rest_framework.generics import ListAPIView

from .serilizers import PretamoSerializer
from .models import Prestamo


class ListarPrestamos(ListAPIView):
    serializer_class = PretamoSerializer
    
    def get_queryset(self):
        lista = Prestamo.objects.listar_prestamo_fecha('2024-03-05')
        
        return lista
