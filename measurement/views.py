from rest_framework import request
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

# from django.db.models import models
from rest_framework.viewsets import ModelViewSet
from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer


class SensorViewSet(ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    @action(methods=['get'], detail=False)
    def all_measurments(self, requests):
        # sensor = Measurement.sensor.get()
        measure = Measurement.sensor.all()
        return Response({'sensors': [{m.value, m.created_at, m.sensor.name} for m in measure]})

class MeasurementViewSet(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
