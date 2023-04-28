from django.db import models
from user_app.models import *
# Create your models here.

class Bolim(models.Model):
    nom=models.CharField(max_length=30)
    rasm=models.FileField(null=True,blank=True,upload_to="bolimlar")
    def __str__(self) -> str:
        return self.nom
    
class Mahsulot(models.Model):
    nom=models.CharField(max_length=30)
    brend=models.CharField(max_length=30)
    holat=models.CharField(max_length=30,default="yang")
    batavsil=models.TextField(blank=True)
    narx=models.PositiveSmallIntegerField()
    chegirma=models.PositiveSmallIntegerField(default=0)
    rasm=models.FileField(null=True,blank=True,upload_to="mahsulot")
    mavjud=models.BooleanField(default=True)
    bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    sotuvchi = models.ForeignKey(Profil,on_delete=models.CASCADE,null=True)
    def __str__(self) -> str:
        return self.nom


class Izoh(models.Model):
    matn=models.CharField(max_length=300)
    reyting=models.PositiveSmallIntegerField(validators=[])
    sana=models.DateField(auto_now_add=True)
    mahsulot=models.ForeignKey(Mahsulot,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.matn

