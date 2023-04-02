from django.db import models

# Create your models here.
class Cargo(models.Model):
    idcargo = models.BigAutoField(primary_key=True) #django coloca el id implicito si no se escribe
    cargo = models.CharField('Cargo', max_length=50)

    def __str__(self) :
        return self.cargo
    

class Empleado(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    correo = models.CharField('Correo', max_length=100)
    sueldo = models.DecimalField('Sueldo', max_digits=8, decimal_places=2)
    activo = models.BooleanField('Activo')
    cargo = models.ForeignKey(Cargo, on_delete=models.RESTRICT)

    def __str__(self):
        return self.nombre + '|' + self.correo + '|'+ self.activo