from rest_framework import serializers

from .models import Prestamo


class PretamoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Prestamo
        fields = ('__all__')