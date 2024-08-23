from django.urls import path
from instamart.views import *


urlpatterns=[
    path('delivery/',delivery,name='delivery')
]