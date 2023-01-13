from django.db import models

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name="id de Categoria")
    nombreCategoria = models.CharField(max_length=70,verbose_name="Nombre de la Categoria")
    def __str__(self):
        return self.nombreCategoria


class Plato(models.Model):
    idPlato = models.IntegerField(primary_key=True,verbose_name="id de Plato")
    nombrePlato = models.CharField(max_length=70,verbose_name="Nombre del Plato")
    valorPlato = models.IntegerField(verbose_name="Valor del Plato")
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombrePlato

  

class Hora(models.Model):
    idHora = models.IntegerField(primary_key=True,verbose_name="id de hora")
    nombreHora = models.CharField(max_length=70,verbose_name="Valor de la hora")
    def __str__(self):
        return self.nombreHora

class Fecha(models.Model):
    idFecha = models.IntegerField(primary_key=True,verbose_name="id de Fecha")
    nombreFecha = models.CharField(max_length=70,verbose_name="Valor de la Fecha")
    def __str__(self):
        return self.nombreFecha

class Reservacion(models.Model):
    idReservacion = models.IntegerField(primary_key=True,verbose_name="id de Reserva")
    nombreReservacion = models.CharField(max_length=70,verbose_name="Nombre del Reservante")
    hora = models.ForeignKey(Hora, on_delete=models.CASCADE)
    fecha = models.ForeignKey(Fecha, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombreReservacion

##########################################

class Bodega(models.Model):
    idProducto = models.IntegerField(primary_key=True,verbose_name="id de Producto")
    nombreProducto = models.CharField(max_length=70,verbose_name="Nombre del Producto")
    cantidadProducto = models.CharField(max_length=70,verbose_name="Cantidad de Producto")
    def __str__(self):
        return self.nombreProducto