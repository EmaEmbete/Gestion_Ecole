from django.db import models


class CodeClient(models.Model):
    code = models.IntegerField()
    montant = models.FloatField(default = 0)
    date = models.DateField(auto_now_add = True)
    etat = models.CharField(max_length = 25, default = "aucun")


    def __int__(self):
        return self.code