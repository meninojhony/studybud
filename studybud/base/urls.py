from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='nome'),
    path('room/', views.room, name='room')
]