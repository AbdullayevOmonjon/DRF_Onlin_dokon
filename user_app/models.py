from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profil(models.Model):
    ism=models.CharField(max_length=25)
    tel=models.CharField(max_length=25)
    jins=models.CharField(max_length=25)
    shahar=models.CharField(max_length=25, blank=True)
    tugulgan_yil=models.PositiveSmallIntegerField()
    rasm=models.FileField(blank=True,null=TimeoutError)
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.ism
    
