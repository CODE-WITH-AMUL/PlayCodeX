from django.urls import path
from .views import *

urlpatterns = [
    path('login/' , login , name='login'),
    path('register/' , register , name='register'),
    path('Treamandconduction/',treamandconduction, name='treamandconduction')
]
