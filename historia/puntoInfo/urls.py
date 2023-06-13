from rest_framework import routers
from .viewsets import PuntoInfoViewSet

router = routers.SimpleRouter()
router.register('puntosInfo', PuntoInfoViewSet)

urlpatterns = router.urls