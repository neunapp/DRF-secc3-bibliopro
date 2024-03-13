from django.db import models

class PrestamoManager(models.Manager):
    
    def listar_prestamo_fecha(self, fecha):
        
         return self.filter(
            date__lte=fecha,
        )