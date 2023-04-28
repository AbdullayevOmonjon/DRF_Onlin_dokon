from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from buyurtma_app.models import *
# Create your views here.

class UserCreateAPIView(APIView):
  def post(self,request):
    serializer=UserSerializers(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  

class ProfilView(APIView):
    # Foydalanuvchilarni ko'rish uchun
    def get(self, request,pk):
        profillar = Profil.objects.filter(id=pk)
        serializer = ProfilSerializer(profillar, many=True)
        return Response(serializer.data)

    # Foydalanuvchini o'zgartirish uchun
    def put(self, request, pk):
        profil = Profil.objects.get(pk=pk)
        serializer = ProfilSerializer(profil, data=request.data)
        if serializer.is_valid():
            # Foydalanuvchini o'zgartirish
            user = profil.user
            if 'password' in request.data:
                user.set_password(request.data['password'])
            user.save()
            # Profilni o'zgartirish
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Foydalanuvchini o'chirish uchun
    def delete(self, request, pk):
        profil = Profil.objects.get(pk=pk)
        # Foydalanuvchini o'chirish
        user = profil.user
        user.delete()
        # Profilni o'chirish
        profil.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ProfilCreateAPIView(APIView):
  def post(self,request):
    serializer=ProfilSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      Savat.objects.create(profil=Profil.objects.last())
      return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  
class LoginAPIView(APIView):
    def post(self, request):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.data['username'],
                password = serializer.data['password']
                         )
            if user is None:
                return Response({"xabar":"Bunaqa user yo'q"}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({"xabar":"Tizimga kirildi"}, status=status.HTTP_200_OK)
        return Response(serializer.errors)
      
      
class LogoutAPIView(APIView):
  def get(self,request):
    logout(request)
    return Response({"xabar":"siz tizimchiqdingiz"},status=status.HTTP_200_OK)