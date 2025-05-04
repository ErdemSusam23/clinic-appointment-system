from django.db import models
from users.models import User

class Appointment(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    )

    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctor_appointments')
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"{self.patient.username} -> {self.doctor.username} at {self.date} {self.time}"
