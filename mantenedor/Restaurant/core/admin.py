from django.contrib import admin
from .models import Categoria, Plato, Reservacion, Hora, Fecha, Bodega
# Register your models here.

admin.site.register(Categoria)
admin.site.register(Plato)
admin.site.register(Reservacion)
admin.site.register(Hora)
admin.site.register(Fecha)
admin.site.register(Bodega)
