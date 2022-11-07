from django.urls import path

from apps.vianda import views

app_name = 'vianda'
urlpatterns = [
    path("registrar", views.registrarVianda, name="registrarVianda"),
    path('listar', views.listarViandas, name='listarViandas')
 ]
