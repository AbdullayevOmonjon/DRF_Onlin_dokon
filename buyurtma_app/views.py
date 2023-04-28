from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

class BuyurtmaAPIView(APIView):
    def get(self,request):
        profil_h=Profil.objects.get(user=request.user)
        buyrtma=Buyurtma.objects.filter(profil=profil_h)
        serializer=BuyurtSerializer(buyrtma,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer=BuyurtSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profil=Profil.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)
    

class SavatitemAPIView(APIView):
  def get(self,request):
    savat=Savat.objects.get(profil__user=request.user)
    savatItm=SavatItm.objects.filter(savat=savat)
    serializer=SavatItmSerializer(savatItm,many=True)
    return Response(serializer.data)
  
  def post(self,request):
    savatItm=request.data
    serializer=SavatItmSerializer(data=savatItm)
    if serializer.is_valid():
      serializer.save(savat=Savat.objects.get(profil__user=request.user))
      return Response(serializer.data)
    return Response(serializer.errors)
  
class SavatItem_U_APIView(APIView):
  def put(self,request,pk):
    savatItem=SavatItm.objects.get(id=pk)
    serializer=SavatItmSerializer(savatItem,data=request.data)
    if serializer.is_valid():
      serializer.save(savat=Savat.objects.get(profil__user=request.user))
      return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
     try:
         savat_itm = SavatItm.objects.get(pk=pk)
         savat_itm.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     except SavatItm.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
       
       
class TanlaganAPIView(APIView):
  def get(self,request):
    profil=Profil.objects.get(user=request.user)
    T=Tanlangan.objects.filter(profil=profil)
    serializer=TanlanganSerializer(T,many=True)
    return Response(serializer.data)
  
  def post(self,request):
    tanlangan=request.data
    serializer=TanlanganSerializer(data=tanlangan)
    if serializer.is_valid():
      serializer.save(profil=Profil.objects.get(user=request.user))
      return Response(serializer.data)
    return Response(serializer.errors)
  
class TanlanganUPAPIView(APIView):
  def put(self, request,pk):
    T=Tanlangan.objects.get(id=pk)
    serializer=TanlanganSerializer(T,data=request.data)
    if serializer.is_valid():
      serializer.save(profil=Profil.objects.get(user=request.user))
      return Response(serializer.data)
    return Response(serializer.errors)
  
  def delete(self, request, pk):
     try:
         tanlangan = Tanlangan.objects.get(pk=pk)
         tanlangan.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
     except SavatItm.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)
    