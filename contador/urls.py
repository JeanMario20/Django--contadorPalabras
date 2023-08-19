from django.urls import path
from . import views

urlpatterns = [
    path('contador/', views.contador, name='contador')
]