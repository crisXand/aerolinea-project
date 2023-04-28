from django.urls import path
from . import views
app_name = 'inicio_app'
urlpatterns = [
    path('', views.inicio, name = 'inicio'),
    path('listarpersonas/',views.listar_personas)
]