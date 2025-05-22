from django.urls import path
from .views import *

urlpatterns = [
    path('',index , name='index'),
    path('Letsgo/',letsgo , name='letsgo'),
    path('question/',question , name='question'),
    path('discribe/',discribe,name='discribe'),
    path('Schedule/', time , name='time'),
    path('info' , info , name='info'),
    
]