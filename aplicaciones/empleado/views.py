from django.shortcuts import render
from .models import Cargo, Empleado
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import EmpleadoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
@method_decorator(login_required, name='dispatch')
class ModificarEmpleado(PermissionRequiredMixin, UpdateView):
    permission_required = ('empleado.change_empleado')
    template_name = "empleados/modificar-empleado.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy("empleados_app:listar-empleados")

class ListarEmpleados(LoginRequiredMixin,ListView):
    template_name = 'empleados/listar-empleados.html'
    model = Empleado
    context_object_name = 'lista_empleados'
    queryset = Empleado.objects.filter(activo=True)
    paginate_by = 5

    def get_queryset(self) :
        nombre = self.request.GET.get('buscar')
        lista_empleado = Empleado.objects.filter(activo=True)
        if nombre :
            lista_empleado = Empleado.objects.filter(nombre__icontains=nombre)

        return lista_empleado
    
# formulario creado por vista generica generado solo con un modelo
class CrearEmpleado2(CreateView):
    model = Empleado
    template_name = "empleados/crear-empleado.html"
    fields = ['nombre', 'correo', 'sueldo', 'activo','cargo']
    success_url = reverse_lazy("empleados_app:listar-empleados")

# formulario creado por vista generica generado solo con un form model
class CrearEmpleado(LoginRequiredMixin,CreateView):
    form_class = EmpleadoForm
    template_name = "empleados/crear-empleado.html"
    success_url = reverse_lazy("empleados_app:listar-empleados")



class EliminarEmpleado(DeleteView):
    template_name = 'empleados/eliminar-empleado.html'
    model = Empleado
    success_url = reverse_lazy('empleados_app:listar-empleados')
