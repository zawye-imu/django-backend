from apis.serializers.tests import TestSerialzier
from apis.models import Test
from rest_framework import viewsets
from rest_framework.decorators import action

class TestViewset(viewsets.ModelViewSet):
    queryset = Test.objects.all() 
    serializer_class = TestSerialzier

    @action(detail=False, methods=['get'])
    def activate_admin(self, request):
        pass