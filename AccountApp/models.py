from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
# Create your models here.

class User(AbstractUser):
    pass

class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6)])
    phone_number = models.CharField(max_length=8)
    specialities = models.ManyToManyField('Speciality', related_name='doctors')
def validate_past_date(value):
    if value >= timezone.localdate():
        raise ValidationError("La date doit être dans le passé.")
class Patient(User):
    national_id = models.CharField(max_length=8, unique=True, validators=[RegexValidator(r'^\d{8}$')])
    phone = models.CharField(max_length=8, validators=[RegexValidator(r'^\d{8}$')])
    birth_date = models.DateField(validators=[validate_past_date])
class Speciality(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)