from django.db import models


class Commande(models.Model):
    CodeCommande = models.IntegerField()
    MontantTotal = models.FloatField()
    DateCommande = models.DateField()
    EtatCommande = models.CharField(max_length = 10)

    def __str__(self):
        return self.CodeCommande