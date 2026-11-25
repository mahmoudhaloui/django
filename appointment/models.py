from django.db import models
# Create your models here.
class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

class Appointment(models.Model):
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reason = models.TextField()
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE)