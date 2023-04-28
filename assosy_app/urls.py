from django.urls import path
from .views import *

urlpatterns = [
  path('bolimlar/',BolimAPIView.as_view(),name="bolimlar"),  
  path('bolim/<int:pk>/mahsulot/',Mahsulot_bolim_APIView.as_view(),name='bolimga_tegishli_mahsulot'),
  path('mahsulot/<int:pk>/',MahsulotU_APIView.as_view(),name='mahsulot'),
  path('mahsulot/<int:pk>/izoh/',Izoh_mahsulot_APIView.as_view(),name='izoh_bita_mahsulot'),
  path('izoh/<int:pk>/',Izoh_updeate_APIView.as_view(),name='izoh_o_u')

]