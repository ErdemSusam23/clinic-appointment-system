from django.urls import path
from .views import PatientAuthView, TokenLoginView

urlpatterns = [
    path('auth/patient/', PatientAuthView.as_view(), name='patient-auth'),
    path('auth/login/', TokenLoginView.as_view(), name='token-login'),
] 