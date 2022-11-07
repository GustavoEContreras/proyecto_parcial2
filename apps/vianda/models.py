from django.contrib.auth.models import User
from django.db import models

from proyecto_parcial2 import settings


# Create your models here.

class TipoPlato(models.Model):
    descripcion = models.CharField(max_length=30)
    activo = models.BooleanField(default=False)

    def __str__(self): # Funcion utilizada para mostrar la descripcion de tipo plato en vez del nombre basico del objeto
        return self.descripcion


class SolicitudVianda(models.Model):
    FRECUENCIA_OPCIONES = {  # Constante utilizada para almacenar las opciones
        ('SEMANAL', 'SEMANAL'),
        ('QUINCELA', 'QUINCENAL')
    }
    frecuencia = models.CharField(max_length=10, choices=FRECUENCIA_OPCIONES, default='SEMANAL')

    MENU_OPCIONES = {
        ('NORMAL', 'NORMAL'),
        ('DIABETICO', 'DIABETICO'),
        ('VEGETARIANO', 'VEGETARIANO')
    }
    tipoMenu = models.CharField(max_length=15, choices=MENU_OPCIONES, default='NORMAL')

    fechaInicioPedidoVianda = models.DateField()

    cantidadViandas = models.IntegerField()

    ESTADO_OPCIONES = {
        ('PENDIENTE', 'PENDIENTE'),
        ('CONFIRMADO', 'CONFIRMADO'),
        ('CANCELADO', 'CANCELADO'),
    }

    estado = models.CharField(max_length=15, choices=ESTADO_OPCIONES, default='PENDIENTE')

    tipoPlato = models.ManyToManyField(TipoPlato)

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.usuario.username + ' - ' + str(self.fechaInicioPedidoVianda)
