from django.db import models
from django.contrib.auth.models import User

class MedicalUser(User):
    SPECIALTIES = (
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
    )
    med_id = models.CharField(max_length = 8, unique=True)
    phone = models.CharField(max_length = 8)
    specialty = models.IntegerField(choices = SPECIALTIES)
    specialty_desc = models.TextField()

class CommonUser(User):
    phone = models.CharField(max_length = 8)
