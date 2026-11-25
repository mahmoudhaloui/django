from django.db import models
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
# Create your models here.
class Status(models.TextChoices):
        PENDING = 'PENDING', 'En attente'
        CONFIRMED = 'CONFIRMED', 'Confirmé'
        CANCELLED = 'CANCELLED', 'Annulé'

class Appointment(models.Model):
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    reason = models.TextField()
    prescription = models.FileField(
    upload_to='prescriptions/',
    blank=True,
    validators=[FileExtensionValidator(['pdf'])]
)
    duration_minutes = models.PositiveIntegerField(default=30)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor = models.ForeignKey('AccountApp.Doctor', on_delete=models.CASCADE)
    patient = models.ForeignKey('AccountApp.Patient', on_delete=models.CASCADE)
    def clean(self):
        super().clean()

        if self.appointment_date:
            old = Appointment.objects.filter(pk=self.pk).first()

            if old is None or old.appointment_date != self.appointment_date:
                if self.appointment_date <= timezone.now():
                    raise ValidationError({
                        'appointment_date': 'La date doit être future.'
                    })
    class Meta:
        ordering = ['appointment_date']

        constraints = [
            models.UniqueConstraint(
                fields=['doctor', 'appointment_date'],
                name='unique_doctor_appointment'
            )
        ]