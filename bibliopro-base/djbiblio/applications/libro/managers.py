from django.db import models


class AutorManager(models.Manager):
    
    def listar_autores_pais(self, pais):
        return self.filter(
            contry=pais
        )