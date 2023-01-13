from django import forms
from django.forms import ModelForm
from .models import Plato, Reservacion, Hora, Fecha, Bodega

class PlatoForm(ModelForm):
    class Meta:
        model = Plato
        fields = ['idPlato','nombrePlato','valorPlato','categoria']

class ReservacionForm(ModelForm):
    class Meta:
        model = Reservacion
        fields = ['idReservacion','nombreReservacion','hora','fecha']

class BodegaForm(ModelForm):
    class Meta:
        model = Bodega
        fields = ['idProducto','nombreProducto','cantidadProducto']


