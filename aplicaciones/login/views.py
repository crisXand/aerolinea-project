from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from .forms import UsuarioNuevoForm
from django.contrib import messages
from django.urls import reverse_lazy
from .forms import UsuarioNuevoForm, LoginForm
from django.views.generic import FormView
from .forms import CaptchForm
# Create your views here.


def nuevo_usuario(request):
    form = UsuarioNuevoForm()
    if request.method == 'POST':
        form = UsuarioNuevoForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio_app:inicio')
    return render(request, 'login/nuevo_usuario.html', context={'form': form})


class LoginUser(FormView):
    form_class = LoginForm
    success_url = reverse_lazy('inicio_app:inicio')
    template_name = 'login/login.html'

    def form_valid(self, form):
        credenciales = form.cleaned_data
        user = authenticate(
            username=credenciales['username'], password=credenciales['password'])

        if 'count' in self.request.session:
            count = self.request.session['count'] + 1
        else:
            count = 1
        self.request.session['count'] = count

        if user is not None:
            login(self.request, user)
                
            return redirect(self.success_url)
        else:
            messages.add_message(self.request, messages.INFO, 'Error: credenciales incorrectas')
            return redirect(reverse_lazy('login_app:login'))


def cerrar_sesion(request):
    logout(request)
    return redirect(reverse_lazy('login_app:login'))
