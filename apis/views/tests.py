from apis.serializers.tests import TestSerialzier
from apis.models import Test
from rest_framework import viewsets

class TestViewset(viewsets.ModelViewSet):
    queryset = Test.objects.all() 
    serializer_class = TestSerialzier