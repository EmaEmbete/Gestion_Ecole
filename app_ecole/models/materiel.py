from django.db import models

class Materiel(models.Model):
    NomMateriel = models.CharField(max_length = 30)
    QnteTotal = models.IntegerField()
    QnteDisponible = models.IntegerField()
    QnteLouer = models.IntegerField()

    def __str__(self):
        return self.NomMateriel