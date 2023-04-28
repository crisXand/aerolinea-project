from django.urls import path
from . import views
app_name = 'empleados_app'
urlpatterns = [
    path('empleado/crear-empleado/', views.CrearEmpleado.as_view(), name = 'crear-empleado'),
    path('empleado/crear-empleado2/', views.CrearEmpleado2.as_view(), name = 'crear-empleado2'),
    path('empleado/listar-empleados/', views.ListarEmpleados.as_view(), name = 'listar-empleados'),
    path('empleado/modificar-empleados/<pk>/', views.ModificarEmpleado.as_view(), name = 'modificar-empleados'),
    path('empleado/eliminar-empleados/<pk>/', views.EliminarEmpleado.as_view(), name = 'eliminar-empleados')


]