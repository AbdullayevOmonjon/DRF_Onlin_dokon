from rest_framework import serializers
from assosy_app.models import *
from .models import *
from user_app.models import *

class TanlanganSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tanlangan
        fields="__all__"

class BuyurtSerializer(serializers.ModelSerializer):
    class Meta:
        model=Buyurtma
        fields="__all__"

class SavatItmSerializer(serializers.ModelSerializer):
    class Meta:
        model=SavatItm
        fields="__all__"

class Savatserializr(serializers.ModelSerializer):
    class Meta:
        model=Savat
        fields="__all__"
        