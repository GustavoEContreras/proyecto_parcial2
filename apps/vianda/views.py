from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.vianda.forms import ViandaForm
from apps.vianda.models import SolicitudVianda


# Create your views here.


# Solo usuarios pueden acceder a esta vista
@login_required(login_url='usuario:login')
def registrarVianda(request):
    nueva_vianda = None
    if request.method == 'POST':  # Si el formulario fue completado
        vianda_form = ViandaForm(request.POST, request.FILES)
        if vianda_form.is_valid():  # Realiza tambien las validaciones definidas en la funcion clean() del ModelForm
            # Se guardan los datos que provienen del formulario en la B.D.
            nueva_vianda = vianda_form.save(commit=False)  # No lo guarda en la B.D
            nueva_vianda.usuario = request.user  # Le pone el usuario que esta logueado en el momento
            nueva_vianda.save()  # Lo guarda
            vianda_form.save_m2m()  # Al haber realizado un save con el atributo commit=False, es necesario invocar a esta función para almacenar el campo many to many (tipoPlato) incluido en la vianda
            messages.success(request,
                             'Se ha agregado correctamente la solicitud de vianda {}'.format(nueva_vianda))
            return redirect(reverse('index'))
    else:
        vianda_form = ViandaForm()  # Si se va a completar el formulario

    context = {  # Variable de contexto
        'form': vianda_form
    }
    return render(request, 'vianda/registrarSolicitudVianda.html', context)


# Solo usuarios pueden acceder a esta vista
@login_required(login_url='usuario:login')
def listarViandas(request):
    viandas = SolicitudVianda.objects.filter(usuario=request.user) # Solo obtiene aquellas viandas las cuales el usuario logueado haya solicitado

    context = { # Variable de contexto
        'viandas': viandas,
    }
    return render(request, 'vianda/listarViandas.html', context)
