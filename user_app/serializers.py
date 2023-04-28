from rest_framework import serializers
from .models import *

class ProfilSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profil
        fields='__all__'


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','password',  ]
        
class LoginUserSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()