from rest_framework import serializers
from measurements.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name', 'latitude', 'longitude', 'created_at', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'value', 'created_at']
