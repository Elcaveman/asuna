from django.urls import path 
from .views import *

urlpatterns = [
    path('about/',about,name="about"),
    path('chat/',chat,name="chat"),
    path('',home,name="home"),
]
