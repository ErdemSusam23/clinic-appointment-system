from django.urls import path
from .views import PatientAuthView

urlpatterns = [
    path('auth/patient/', PatientAuthView.as_view(), name='patient-auth'),
] 