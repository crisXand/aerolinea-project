from django.urls import path
from . import views

urlpatterns = [
    path('inicio/hola/', views.inicio)
    
]