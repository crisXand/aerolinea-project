from django.urls import path, include
from . import views
app_name = 'login_app'

urlpatterns = [
    path('login/nuevo-usuario/', views.nuevo_usuario, name = 'nuevo-usuario'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.cerrar_sesion, name = "logout"),
    path('locked/', views.locked, name = "locked")

]