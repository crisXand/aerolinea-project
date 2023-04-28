from django.contrib import admin
from .models import Empleado, Cargo


#custom
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','correo', 'sueldo', 'activo')
    search_fields = ('nombre', 'correo')
    list_filter = ('cargo','activo')

# Register your models here.
admin.site.register(Empleado, EmpleadosAdmin)
admin.site.register(Cargo)

