from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True)
    phone_number = models.CharField(max_length=8)
    specialities = models.ManyToManyField('Speciality', related_name='doctors')
def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("La date doit être dans le passé.")
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True)
    phone = models.CharField(max_length=8)
    birth_date = models.DateField(
        validators=[validate_past_date]
    )

class Speciality(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)