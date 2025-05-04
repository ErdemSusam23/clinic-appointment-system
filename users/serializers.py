from rest_framework import serializers
from .models import User
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class PatientAuthSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=150)
    last_name = serializers.CharField(max_length=150)
    date_of_birth = serializers.DateField()

    def validate(self, data):
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        date_of_birth = data.get('date_of_birth')

        try:
            user = User.objects.get(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                role='patient'
            )
            return {'user': user}
        except User.DoesNotExist:
            raise serializers.ValidationError('Invalid credentials')
