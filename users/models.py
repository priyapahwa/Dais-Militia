from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.core.exceptions import ValidationError




mult = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 0, 6, 7, 8, 9, 5], [2, 3, 4, 0, 1, 7, 8, 9, 5, 6],
        [3, 4, 0, 1, 2, 8, 9, 5, 6, 7], [4, 0, 1, 2, 3, 9, 5, 6, 7, 8], [5, 9, 8, 7, 6, 0, 4, 3, 2, 1],
        [6, 5, 9, 8, 7, 1, 0, 4, 3, 2], [7, 6, 5, 9, 8, 2, 1, 0, 4, 3], [8, 7, 6, 5, 9, 3, 2, 1, 0, 4],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]
perm = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 5, 7, 6, 2, 8, 3, 0, 9, 4], [5, 8, 0, 3, 7, 9, 6, 1, 4, 2],
        [8, 9, 1, 6, 0, 4, 3, 5, 2, 7], [9, 4, 5, 3, 1, 2, 6, 8, 7, 0], [4, 2, 8, 6, 5, 7, 3, 9, 0, 1],
        [2, 7, 9, 3, 8, 0, 6, 4, 1, 5], [7, 0, 4, 6, 9, 1, 3, 2, 5, 8]]

def validateAadharNo(aadhar_number):
    if (len(aadhar_number) == 12 and aadhar_number.isdigit()):
        Validate(aadhar_number)
    else:
        raise ValidationError("Invalid Aadhar Number")
def Validate(aadhar_number):
    try:
        i = len(aadhar_number)
        j = 0
        x = 0

        while i > 0:
            i -= 1
            x = mult[x][perm[(j % 8)][int(aadhar_number[i])]]
            j += 1
        if x == 0:
            pass
        else:
            raise ValidationError("Invalid Aadhar Number")

    except:
        raise ValidationError('Invalid Aadhar Number')

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    birth_date = models.DateField(null=True, blank=True)
    mobile_regex = RegexValidator(regex=r'^(\+91[\-\s]?)?[0]?(91)?[6789]\d{9}$', message="Invalid Mobile Number")
    mobile_number = models.CharField(max_length=10, unique=True, validators=[mobile_regex])
    aadhar_number = models.CharField(max_length=16, unique=True,validators=[validateAadharNo])
