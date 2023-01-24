from django.db import models



class Client(models.Model):
    NomClient = models.CharField(max_length=20)
    Adress = models.CharField(max_length = 50)
    Telephone = models.CharField(max_length = 13)
    Email = models.EmailField(max_length = 100)
    MotPass = models.CharField(max_length = 32)
    CodeConfirmation = models.IntegerField()


    def __str__(self):

        return self.NomClient

    class Meta:
        db_table = 'app_ecole_client'
