from django.db import models
from django.db.models import Sum
from assosy_app.models import *
from user_app.models import *

# Create your models here.
class Tanlangan(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)

class Savat(models.Model):
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    sana=models.DateField(auto_now_add=True,null=True )


class SavatItm(models.Model):
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    miqdor=models.PositiveSmallIntegerField(default=1)
    sana=models.PositiveSmallIntegerField(default=True)
    savat=models.ForeignKey(Savat,on_delete=models.Case,related_name="itemlari")
    ummumiy_summa=models.IntegerField(null=True,blank=True)
    yetkazish_puli=models.PositiveSmallIntegerField(default=15000)

    def save(self,*args,**kwargs):
        narx=self.mahsulot.narx-(self.mahsulot.narx*self.mahsulot.chegirma/100)
        self.ummumiy_summa=self.miqdor*narx+self.yetkazish_puli
        super().save(*args,**kwargs)

class Buyurtma(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    savat=models.ForeignKey(Savat,on_delete=models.CASCADE)
    holat=models.CharField(max_length=25)
    sana=models.DateField(auto_now_add=True)
    summa=models.PositiveSmallIntegerField(blank=True)


    def save(self,*args,**kwargs):
        itemlar=self.savat.itemlari.all()
        self.summa=itemlar.aggregate(summasi=Sum('ummumiy_summa')).get("summasi")
        super().save(*args,**kwargs)