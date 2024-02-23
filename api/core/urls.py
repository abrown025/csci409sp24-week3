from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import AirportViewSet, RunwaysViewSet, AirlineViewSet, FlightsViewSet

router = DefaultRouter()
router.register(r'airport', AirportViewSet)
router.register(r'airlines', AirlineViewSet)
router.register(r'runways', RunwaysViewSet)
router.register(r'flights', FlightsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]