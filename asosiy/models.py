from django.db import models
from accounts.models import Ombor

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    brend = models.CharField(max_length=50)
    olchov = models.CharField(max_length=50)
    narx = models.PositiveIntegerField(default=True)
    miqdor = models.PositiveIntegerField(default=True)
    kelgan_sana = models.DateField(null=True, blank=True)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom}, {self.brend}"

class Mijoz(models.Model):
    ism = models.CharField(max_length=30)
    nom = models.CharField(max_length=30)
    manzil = models.CharField(max_length=30)
    tel = models.CharField(max_length=30)
    qarz = models.PositiveIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.ism}, {self.nom}"

