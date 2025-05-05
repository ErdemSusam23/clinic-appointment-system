from rest_framework import serializers
from .models import Department, DoctorProfile
from users.models import User

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']

class DoctorProfileSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    class Meta:
        model = DoctorProfile
        fields = ['id', 'user', 'department']
