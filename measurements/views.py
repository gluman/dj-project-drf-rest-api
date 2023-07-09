from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from models import Project, Measurement

@api_view(['POST', 'PATCH'])
class ProjectViewSet(ModelViewSet):
    if request.method == 'POST':
        pass
    if request.method == 'PATCH':
        name = Project.objects.all()


    """ViewSet для проекта."""
    # TODO: добавьте конфигурацию для объекта

@api_view(['GET', 'POST'])
class MeasurementViewSet(ModelViewSet):
    if request.method == 'GET':
        pass
    if request.method == 'POST':
        pass

    """ViewSet для измерения."""
    # TODO: добавьте конфигурацию для измерения
