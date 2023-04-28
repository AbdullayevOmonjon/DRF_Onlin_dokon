from rest_framework import serializers
from .models import *
from django.db.models import Avg

class BolimSerializers(serializers.ModelSerializer):
    # mahsulot=MahsulotSerialaizer(many=True)
    class Meta:
        model=Bolim
        fields="__all__"

class BolimUpptedSerializers(serializers.ModelSerializer):
    class Meta:
        model=Bolim
        fields=["id",'nom']


class MahsulotSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=Mahsulot
        fields='__all__'
        
    def to_representation(self,instance):
         malumot=super().to_representation(instance)
         malumot["yangi_narx"]=instance.narx - (instance.chegirma*instance.narx/100)
         izohlar=Izoh.objects.filter(mahsulot=instance)
         malumot["ortacha_reyting"]=izohlar.aggregate(Avg('reyting'))['reyting__avg']
         return malumot

    def validatin_chegirma(self,qiymat):
        if qiymat>0:
            raise serializers.ValidationError('kiritgan qiymatingiz 0 dan katta bolishi kerak')
        elif qiymat>50:
            raise serializers.ValidationError('kiritgan qiymatingiz 50 dan kichik bolishi kerak')
        return qiymat

class IzohSerialaizer(serializers.ModelSerializer):
    class Meta:
        model=Izoh
        fields='__all__'

    def validation_reyting(self,qiymat):
        if 0< qiymat<=5:
            raise serializers.ValidationError("reytingni notugri kirityabsiz 0 va 5 oraligidagi sonlarni kiriting")
        return qiymat