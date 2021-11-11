from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$', message="Invalid Mobile Number")
    mobile_number = models.CharField(max_length=10, unique=True, validators=[mobile_regex])
    aadhar_number = models.CharField(max_length=16, unique=True)
