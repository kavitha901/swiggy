from django.urls import path
from food.views import *

urlpatterns=[
    path('delivery/',delivery,name='delivery')
]