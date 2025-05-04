from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

# DRF Router auto-generates RESTful routes for your ViewSet
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
