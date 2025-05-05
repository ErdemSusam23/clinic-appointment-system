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

        # First check if any patient exists with this name
        name_matches = User.objects.filter(
            first_name=first_name,
            last_name=last_name,
        )
        
        if not name_matches.exists():
            raise serializers.ValidationError('No patient found with this name')
            
        # Then check if the patient with this name has matching DOB
        dob_matches = name_matches.filter(date_of_birth=date_of_birth)
        if not dob_matches.exists():
            raise serializers.ValidationError('Date of birth does not match')
            
        # Finally check if this person is a patient
        patient_matches = dob_matches.filter(role='patient')
        if not patient_matches.exists():
            raise serializers.ValidationError('Person found but not a patient')
            
        return {'user': patient_matches.first()}
