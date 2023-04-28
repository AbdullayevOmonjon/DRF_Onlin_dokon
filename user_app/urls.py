from django.urls import path
from .views import *

urlpatterns = [
  path('userCreat/',UserCreateAPIView.as_view(),name='usercreate'),
  path('profil/create/',ProfilCreateAPIView.as_view(),name='profilcreate'),
  path('profil/<int:pk>/',ProfilView.as_view(),name='profil'),
  path('login/',LoginAPIView.as_view(),name='login'),
  path('logout/',LogoutAPIView.as_view(),name='logout'),
]