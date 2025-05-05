from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet, MyAppointmentsView

# DRF Router auto-generates RESTful routes for your ViewSet
router = DefaultRouter()
router.register(r'appointments', AppointmentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('appointments/my/', MyAppointmentsView.as_view(), name='my-appointments'),
]
