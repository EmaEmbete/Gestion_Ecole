from django.db import models
from app_ecole.models import Client


class CommandeClient(models.Model):
    client = models.ForeignKey(Client, on_delete = models.CASCADE)
    CodeCommande = models.IntegerField()
    MontantTotal = models.FloatField()
    DateCommande = models.DateField()
    EtatCommande = models.CharField(max_length = 10)

    def __int__(self):
        return self.CodeCommande