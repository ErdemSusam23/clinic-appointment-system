from django.db import models
from users.models import User

class DoctorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} ({self.department.name})"

class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
