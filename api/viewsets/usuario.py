# django
from django.db import transaction

# Rest framework
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.decorators import action

# Models
from api.models import Usuario
from api.models.servicio import Servicio

# Serializer
from api.serializers import UsuarioBaseSerializer, UsuarioReadSerializer, UsuarioSaveSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioReadSerializer
    queryset = Usuario.objects.filter(active=True)

    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombre",)
    search_fields = ("nombre",)
    ordering_fields = ("id", "nombre")

    def get_serializer_class(self):
        """Define serializer for API"""
        async_options = self.request.query_params.get('async_options', False)
        if async_options:
            return UsuarioBaseSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return UsuarioReadSerializer
        else:
            return UsuarioSaveSerializer

    def create(self, request, *args, **kwargs):
        user = request.user.id
        data = request.data
        data['createdBy'] = user # user who created the record 

        with transaction.atomic():
            serializer = self.get_serializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

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
    
    @action(methods=["get"], detail=False)
    def servicio(self, request, *args, **kwargs):
        id_servicio = request.query_params.get('id', None)
        user = Servicio.objects.get(id=id_servicio).usuario
        serializer = UsuarioReadSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)