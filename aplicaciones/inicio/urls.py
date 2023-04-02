from django.urls import path
from . import views

urlpatterns = [
    path('hola/', views.inicio),
    path('listarpersonas/',views.listar_personas)
]