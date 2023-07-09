from rest_framework import serializers

from measurements.models import Project


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'latitude', 'longitude', 'created_at']

