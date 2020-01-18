from django.db import models
from django.contrib.auth.models import User


class UserRoles(models.Model):
    ROLES = (
        (1, 'Paciente'),
        (2, 'Médico'),

    )
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None
    )
    role = models.IntegerField(choices=ROLES, default=1)


class MedService(models.Model):
    SPECIALTIES = (
        (1, 'Small'),
        (2, 'Medium'),
        (3, 'Large'),
    )
    med_id = models.CharField(max_length=8, unique=True, default='')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None
    )
    specialty = models.IntegerField(choices=SPECIALTIES, default=1)
    specialty_desc = models.TextField()
