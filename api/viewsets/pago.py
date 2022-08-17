# django
from tokenize import Number
from django.db import transaction

# Rest framework
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from api import serializers

# Models
from api.models import Pago, Servicio, Configuracion

# Serializer
from api.serializers import PagoBaseSerializer, PagoReadSerializer, PagoSaveSerializer


class PagoViewSet(viewsets.ModelViewSet):
    serializer_class = PagoReadSerializer
    queryset = Pago.objects.filter(active=True)

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ('servicio',)
    search_fields = ("nombre",)
    ordering_fields = ("id", "nombre")

    def get_serializer_class(self):
        """Define serializer for API"""
        async_options = self.request.query_params.get('async_options', False)
        if async_options:
            return PagoBaseSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return PagoReadSerializer
        else:
            return PagoSaveSerializer

    def create(self, request, *args, **kwargs):
        user = request.user.id
        data = request.data
        data['createdBy'] = user # user who created the record 




        with transaction.atomic():
            instancia_servicio = Servicio.objects.get(id=data['servicio'])
            pago_anio = instancia_servicio.anio
            pago_mes = instancia_servicio.mes
            mesesPagar = int( data.get('meses_a_pagar', 0) )
            pago_anio_actual = pago_anio
            pago_mes_actual = pago_mes

            if (pago_mes + mesesPagar) > 12:
                pago_anio += 1
                pago_mes = (pago_mes + mesesPagar) - 12
            else:
                pago_mes += mesesPagar

            instancia_servicio.anio = pago_anio
            instancia_servicio.mes = pago_mes
            instancia_servicio.save()

            costo_mensual_agua = 0
            try:
                configuraciones = Configuracion.objects.all().last()
                costo_mensual_agua =  configuraciones.cuota_agua
            except Exception as e:
                return Response({"message": "No se pudo obtener la configuracion"}, status=status.HTTP_400_BAD_REQUEST)


            for i in range(mesesPagar):
                if pago_mes_actual >= 12:
                    pago_mes_actual += 1
                    pago_anio_actual += 1
                    pago_mes_actual = pago_mes_actual - 12
                else:
                    pago_mes_actual += 1

                instancia_pago = Pago.objects.create(
                    servicio=instancia_servicio,
                    anio=pago_anio_actual,
                    mes=pago_mes_actual,
                    descripcion=data.get('descripcion', ''),
                    pago=costo_mensual_agua
                )
                
        serializer = self.get_serializer(instancia_pago)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        usuario = request.user.id
        data = request.data
        instance = self.get_object()
        data['updatedBy'] = usuario # user who updated the record

        with transaction.atomic():
            serializer = self.get_serializer(instance, data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)