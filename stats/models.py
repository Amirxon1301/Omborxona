from django.db import models
from accounts.models import Ombor
from asosiy.models import Mahsulot, Mijoz
# Create your models here.
class Statistika(models.Model):
    mahsulot= models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveIntegerField()
    summa = models.PositiveIntegerField()
    talangan_summa = models.PositiveIntegerField()
    nasiya = models.PositiveIntegerField(default=0)
    sana = models.DateField()
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mijoz} ning statistikasi"