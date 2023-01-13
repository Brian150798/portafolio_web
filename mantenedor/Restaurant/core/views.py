from django.shortcuts import render, redirect
from .models import Plato, Reservacion, Hora, Fecha, Bodega
from core.forms import PlatoForm, ReservacionForm, BodegaForm
# Create your views here.
def home(request):
    platos = Plato.objects.all()
    contexto = {
        'platos':platos
    }
    return render(request,'core/home.html', contexto)

def form_plato(request):
    formulario = PlatoForm()
    
    contexto = {
        'form':PlatoForm()
    }
    if request.method == 'POST':
        formulario = PlatoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_plato.html', contexto)

def form_mod_plato(request,id):
    plato = Plato.objects.get(idPlato = id)

    contexto = {
        'form' : PlatoForm(instance=plato)
    }

    if request.method == 'POST':
        formulario = PlatoForm(data=request.POST,instance=plato)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_plato.html',contexto)

def form_del_plato(request,id):
    plato = Plato.objects.get(idPlato = id)

    plato.delete()

    return redirect (to="home")


    ###########################################


def reserva(request):
    reservas = Reservacion.objects.all()
    contexto = {
        'reservas':reservas
    }
    return render(request,'core/reserva.html', contexto)

def form_reserva(request):
    formulario = ReservacionForm()
    
    contexto = {
        'form':ReservacionForm()
    }
    if request.method == 'POST':
        formulario = ReservacionForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_reserva.html', contexto)

def form_mod_reserva(request,id):
    reservacion = Reservacion.objects.get(idReservacion= id)

    contexto = {
        'form' : ReservacionForm(instance=reservacion)
    }

    if request.method == 'POST':
        formulario = ReservacionForm(data=request.POST,instance=reservacion)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_reserva.html',contexto)

def form_del_reserva(request,id):
    reserva = Reservacion.objects.get(idReservacion = id)

    reserva.delete()

    return redirect (to="reserva")


##########################################

def bodega(request):
    bodegas = Bodega.objects.all()
    contexto = {
        'bodegas':bodegas
    }
    return render(request,'core/bodega.html', contexto)

def form_bodega(request):
    formulario = BodegaForm()
    
    contexto = {
        'form':BodegaForm()
    }
    if request.method == 'POST':
        formulario = BodegaForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Guardado Correctamente"
    return render(request,'core/form_bodega.html', contexto)

def form_mod_bodega(request,id):
    bodega = Bodega.objects.get(idProducto= id)

    contexto = {
        'form' : BodegaForm(instance=bodega)
    }

    if request.method == 'POST':
        formulario = BodegaForm(data=request.POST,instance=bodega)
        if formulario.is_valid:
            formulario.save()
            contexto['mensaje'] = "Modificado Correctamente"


    return render (request, 'core/form_mod_bodega.html',contexto)

def form_del_bodega(request,id):
    bodega = Bodega.objects.get(idProducto = id)

    bodega.delete()

    return redirect (to="bodega")

