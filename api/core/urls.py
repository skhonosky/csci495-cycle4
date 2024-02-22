from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AirportViewSet
from .views import AirlineViewSet
from .views import FlightViewSet
from .views import RunwayViewSet

router = DefaultRouter()
router.register(r'airports/', AirportViewSet)
router.register(r'airlines/', AirlineViewSet)
router.register(r'flgihts/', FlightViewSet)
router.register(r'runways/', RunwayViewSet)

urlpatterns = [
    path(' ', include(router.urls)),
]