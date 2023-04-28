from django.urls import path
from .views import *

urlpatterns = [
   path('',BuyurtmaAPIView.as_view(),name='buyurtmalar'),
   path('savatitm/',SavatitemAPIView.as_view(),name='savatItm'),
   path('savatitm/<int:pk>/',SavatItem_U_APIView.as_view(),name='savatItmU'),
   path('tanlangan/',TanlaganAPIView.as_view(),name='Tanlangan mahsulot'),
   path('tanlangan/<int:pk>/',TanlanganUPAPIView.as_view(),name='Tanlangan_mahsulot_ozgartirish'),
]