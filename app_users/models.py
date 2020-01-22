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
        default=None,
        related_name='role'
    )
    role = models.IntegerField(choices=ROLES, default=1)


class UserPhones(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
        related_name='phone'
    )
    phone = models.TextField()


class MedService(models.Model):
    SPECIALTIES = (
        (1, 'Anatomía Patológica'),
        (2, 'Alergología'),
        (3, 'Cardiología'),
        (4, 'Dermatología'),
        (5, 'Endocrinilogía'),
        (6, 'Gastroenterología'),
        (7, 'Geriatría'),
        (8, 'Hematología'),
        (9, 'Enfermedades infecciosas'),
        (10, 'Neumología'),
        (11, 'Neurología'),
        (12, 'Oftalmología'),
        (13, 'Otorrinolaringología'),
        (14, 'Pediatría'),
        (15, 'Psiquiatría'),
        (16, 'Rehabilitación'),
        (17, 'Reumatología'),
        (18, 'Traumatología')
    )
    med_id = models.CharField(max_length=8, unique=True, default='')
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
        related_name='service'
    )
    specialty = models.IntegerField(choices=SPECIALTIES, default=1)
    specialty_desc = models.TextField()
    PROVINCES = (
        (1, 'San José'),
        (2, 'Alajuela'),
        (3, 'Heredia'),
        (4, 'Cartago'),
        (5, 'Guanacaste'),
        (6, 'Puntarenas'),
        (7, 'Limón'),
    )
    province = models.IntegerField(choices=PROVINCES, default=1)
    address = models.TextField()
    

    
