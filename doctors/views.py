from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Department, DoctorProfile
from .serializers import DepartmentSerializer, DoctorProfileSerializer

# Create your views here.

class DepartmentListView(ListAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DepartmentDoctorsView(ListAPIView):
    serializer_class = DoctorProfileSerializer

    def get_queryset(self):
        department_id = self.kwargs['pk']
        return DoctorProfile.objects.filter(department_id=department_id)
