from rest_framework import request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from models import Project, Measurement

# @api_view(['POST', 'PATCH'])
# class ProjectViewSet(ModelViewSet):
#     if request.method == 'POST':
#         pass
#     if request.method == 'PATCH':
#         pass


class ProjectView(APIView):

    def get(self, request):
        pass
    def post(self, request):
        pass

    def patch(self, request):
        pass

# @api_view(['GET', 'POST'])
# class MeasurementViewSet(ModelViewSet):
#     if request.method == 'GET':
#         pass
#     if request.method == 'POST':
#         pass

class MeasurementView(APIView):
    def post(self, request):
        pass

