from django.urls import path
from rest_framework import routers
from measurement.views import SensorViewSet, MeasurementViewSet

route_sensor = routers.DefaultRouter()
route_sensor.register('sensors', SensorViewSet)
route_measurement = routers.SimpleRouter()
route_measurement.register('measurement', MeasurementViewSet)

urlpatterns = [

]
urlpatterns += route_sensor.urls
urlpatterns += route_measurement.urls