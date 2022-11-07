from django.contrib import admin

from apps.vianda.models import SolicitudVianda, TipoPlato

# Register your models here.

admin.site.register(SolicitudVianda)
admin.site.register(TipoPlato)