from django.db import models
from app_ecole.models import CommandeClient, Materiel


class DetailCommande(models.Model):
    materiel = models.ForeignKey(Materiel, on_delete = models.CASCADE)
    commandeclient = models.ForeignKey(CommandeClient, on_delete = models.CASCADE)
    QnteDemande = models.IntegerField()
    PrixUnit = models.IntegerField()
    Montant = models.IntegerField()
    NbreJour = models.IntegerField()
    DateDebut = models.DateField()

    
