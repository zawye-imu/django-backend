from rest_framework import serializers
from apis.models import Test

class TestSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = ["id","name"]