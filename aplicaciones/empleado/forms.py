from django import forms
from django.forms import ModelForm

from .models import Empleado

class EmpleadoForm(ModelForm):
    correo = forms.EmailField(max_length=200)
    class Meta:
        model = Empleado
        fields = ['nombre', 'correo', 'sueldo', 'activo', 'cargo']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'})
        }
    def clean_correo(self) :
        email = self.cleaned_data['correo']
        lista = Empleado.objects.filter(correo = email).exclude(id = self.instance.id)
        print(self.instance.id)
        if lista:
            self.add_error('correo', 'El correo ya existe')

        if not email.endswith(('gmail.com', 'yahoo.com')):
            self.add_error('correo', 'El dominio no es valido')
        return email