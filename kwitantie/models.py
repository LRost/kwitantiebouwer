from django.db import models


# Create your models here.
class Kwitantie(models.Model):
    kwitantienummer = models.CharField(max_length=20, default='')
    bedrag = models.IntegerField(default=0)
    aantal_uren = models.CharField(max_length=20, default='')
    project = models.CharField(max_length=200, default='')
    beschrijving = models.CharField(max_length=700, default='')
    dienst = models.CharField(max_length=40, default='')
    naam = models.CharField(max_length=200, null=False)
    straat = models.CharField(max_length=200, default='', null=False)
    nummer = models.CharField(max_length=20, default='', null=False)
    toevoeging = models.CharField(max_length=20, default='', blank=True)
    postcode = models.CharField(max_length=10, null=False)
    plaats = models.CharField(max_length=100, null=False)
    land = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.kwitantienummer


