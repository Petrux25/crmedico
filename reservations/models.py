from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    med = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
        default=None,
        related_name='schedule'
    )


class Time(models.Model):
    time = models.TextField()
    schedule = models.ForeignKey(
        Schedule, on_delete=models.CASCADE, related_name='times')


class Appointments(models.Model):
    date = models.TextField()
    time = models.ForeignKey(Time, on_delete=models.CASCADE, related_name='appointment')
    reserved = models.BooleanField(default=False)
    patient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointment')
