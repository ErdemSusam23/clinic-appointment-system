from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
        ('admin', 'Admin'),
    )
    
    # Remove email field
    email = None
    
    # Make first_name and last_name required
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    date_of_birth = models.DateField()
    
    # Use username as the USERNAME_FIELD
    USERNAME_FIELD = 'username'
    # Required fields for creating a user
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_of_birth', 'role']
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
