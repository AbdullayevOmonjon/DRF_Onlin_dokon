from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet 
from rest_framework import filters
# Create your views here.


class BolimAPIView(APIView):
    def get(self,request):
        if request.user.is_authenticated:
            bolim=Bolim.objects.all()
            serializer=BolimSerializers(bolim, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({"xabar":"login qilinmagan!"})
    
class Mahsulot_bolim_APIView(APIView):
    def get(self,request,pk):
        mahsulot=Mahsulot.objects.filter(bolim__id=pk)
        serializer=MahsulotSerialaizer(mahsulot,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request,pk):
        try:
            bolim = Bolim.objects.get(id=pk) # get the product for which the comment is being made
        except Mahsulot.DoesNotExist:
            return Response({'error': 'Mahsulot not found'})
        
        data = {'bolim': bolim.id, 'profil': request.user.profil.id}
        data.update(request.data) # add the comment data to the request data
        
        serializer = MahsulotSerialaizer(data=data)
        if serializer.is_valid():
            serializer.save() # save the new comment
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
  
    
class MahsulotU_APIView(APIView):
    def get(self,request,pk):
        mahsulot=Mahsulot.objects.filter(id=pk)
        serializer=MahsulotSerialaizer(mahsulot,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    def put(self,request,pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        serializer=MahsulotSerialaizer(mahsulot,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        if Mahsulot.objects.filter(profil__user=request.user):
            mahsulot.delete()
            return Response({"Xabar":"Mahsulot ochirildi"})
        return Response({"Xabar":"xatoli yuz berdi"})

     
class Izoh_mahsulot_APIView(APIView):
    def get(self,request,pk):
        izoh=Izoh.objects.filter(mahsulot__id=pk)   
        serializer=IzohSerialaizer(izoh,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self, request, pk):
        try:
            mahsulot = Mahsulot.objects.get(id=pk) # get the product for which the comment is being made
        except Mahsulot.DoesNotExist:
            return Response({'error': 'Mahsulot not found'})
        
        data = {'mahsulot': mahsulot.id, 'profil': request.user.profil.id}
        data.update(request.data) # add the comment data to the request data
        
        serializer = IzohSerialaizer(data=data)
        if serializer.is_valid():
            serializer.save() # save the new comment
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class Izoh_updeate_APIView(APIView):   
    def put(self,request,pk):
        izoh=Izoh.objects.get(id=pk)
        serializer=IzohSerialaizer(izoh,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def delete(self,request,pk):
        izoh=Izoh.objects.get(id=pk)
        if Profil.objects.filter(user=request.user):
            izoh.delete()
            return Response({'xabar':"malumot ochirildi"})
        return Response({"xabar":"malumot ochirilmadi"})


        
    
