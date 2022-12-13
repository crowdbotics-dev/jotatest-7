from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AzulViewSet,CasaViewSet,PisoViewSet,PuertasViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register('casa', CasaViewSet )
router.register('puertas', PuertasViewSet )
router.register('piso', PisoViewSet )
router.register('azul', AzulViewSet )

urlpatterns = [
    path("", include(router.urls)),
]
