import datetime

from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.forms import DateInput
from apps.vianda.models import SolicitudVianda


class ViandaForm(ModelForm): # ModelForm basado en SolicitudVianda
    class Meta:
        model = SolicitudVianda
        fields = ('frecuencia', 'tipoMenu', 'fechaInicioPedidoVianda', 'cantidadViandas', 'tipoPlato') # Aquellos campos que el usuario puede elegir a su favor

        widgets = { # Permite que la fecha se represente como un input date en HTML
            'fechaInicioPedidoVianda': DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }

    def clean(self): # Función utilizada para validar datos
        cleaned_data = super().clean()
        fechaInicioPedidoVianda = cleaned_data.get("fechaInicioPedidoVianda")
        fechaActual = datetime.date.today() # Fecha actual

        cantidadViandas = cleaned_data.get('cantidadViandas')

        tipoPlato = cleaned_data.get('tipoPlato')
        # Verificar que la fecha sea posterior a la actual
        if fechaActual > fechaInicioPedidoVianda:
            raise ValidationError(
                {
                    'fechaInicioPedidoVianda': 'La fecha de inicio de pedido de vianda no puede ser anterior a la fecha actual'},
                code='Invalido'
            )
        # Verificar que la cantidad de viandas sea al menos 1
        elif cantidadViandas < 1:
            raise ValidationError(
                {'cantidadViandas': 'La cantidad de viandas no puede ser menor a 1'}, code='Invalido'
            )
        # Verificar que se elija al menos un tipo de plato
        elif tipoPlato.count() < 1:
            raise ValidationError(
                {'tipoPlato': 'Debe elegirse al menos un tipo de plato'}, code='Invalido'
            )
        return cleaned_data # Devuelve la información del formulario





