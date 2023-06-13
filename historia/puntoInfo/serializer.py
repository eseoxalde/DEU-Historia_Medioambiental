from .models import PuntoInfo
from rest_framework import serializers

class PuntoInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PuntoInfo
        fields = '__all__'
        