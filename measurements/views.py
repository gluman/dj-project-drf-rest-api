from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from models import Project, Measurement

@api_view(['GET', 'POST'])
class ProjectViewSet(ModelViewSet):
    if request.method == 'GET':
        name = Project.objects.all()
    if request.method == 'POST':
        pass


    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта

@api_view(['GET', 'POST'])
class MeasurementViewSet(ModelViewSet):
    if req
    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
