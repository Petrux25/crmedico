from django.shortcuts import render
from app_users.models import MedService
from django.contrib.auth.models import User
from .models import Time
from django.http import JsonResponse


def create(request, med_id):
    med = User.objects.filter(username=med_id)[0]

    return render(request, "create.html", {"med": med})


def get_times(request):
    times = Time.objects.exclude(appointment__date=request.POST['date'])
    times = list(map(to_time, times))

    return JsonResponse(times, safe=False)


def to_time(time):
    print(time)
    return {"id": time.id, "time": time.time}


def save_appointment(request):

    current_user = request.user
    medId = request.POST['usr']
    med = User.objects.filter(username=med_id)[0]
    date = request.POST['date']
    time = time(request.POST['time'])

    appointment = Appointments(
        date=date, time=time, reserved=True,med=med, patient=current_user)
    appointment.save()
