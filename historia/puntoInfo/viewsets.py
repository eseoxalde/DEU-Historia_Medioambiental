from .models import PuntoInfo
from .serializer import PuntoInfoSerializer
from rest_framework import viewsets

class PuntoInfoViewSet(viewsets.ModelViewSet):
    queryset = PuntoInfo.objects.all()
    serializer_class = PuntoInfoSerializer