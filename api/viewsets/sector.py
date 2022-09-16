# django
from django.db import transaction

# Rest framework
from rest_framework import viewsets, filters, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

# Models
from api.models import Sector

# Serializer
from api.serializers import SectorBaseSerializer, SectorReadSerializer, SectorSaveSerializer
from api.permissions.user import UserCajeroAdminPermissions
from rest_framework.permissions import IsAuthenticated

class SectorViewSet(viewsets.ModelViewSet):
    serializer_class = SectorReadSerializer
    queryset = Sector.objects.filter(active=True)
    permission_classes = [IsAuthenticated, UserCajeroAdminPermissions]
    
    filter_backends = (DjangoFilterBackend,
                       filters.SearchFilter, filters.OrderingFilter)
    filter_fields = ("nombre",)
    search_fields = ("nombre",)
    ordering_fields = ("id", "nombre")

    def get_serializer_class(self):
        """Define serializer for API"""
        async_options = self.request.query_params.get('async_options', False)
        if async_options:
            return SectorBaseSerializer
        if self.action == 'list' or self.action == 'retrieve':
            return SectorReadSerializer
        else:
            return SectorSaveSerializer

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
