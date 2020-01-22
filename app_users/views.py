from django.shortcuts import render, redirect
from .forms import UserForm
from .models import MedService, UserRoles, UserPhones
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from reservations.models import *

def register(request, usr_type):
    specialties = MedService.SPECIALTIES
    provinces = MedService.PROVINCES
    return render(request, "register.html", {'usr_type': usr_type, 'specialties': specialties, 'provinces': provinces})


def create(request, usr_type):
    is_user_med = (usr_type == "med")
    user_role = 2 if is_user_med else 1
    form = UserForm(request.POST)
    if form.is_valid():
        user_instance = form.save(commit=False)
        user_instance.set_password(request.POST['password'])
        user_instance.save()
        phone_instance = UserPhones(
            user=user_instance, phone=request.POST['phone'])
        phone_instance.save()
        role_instance = UserRoles(user=user_instance, role=user_role)
        role_instance.save()

        if is_user_med:
            med_service = MedService(med_id=request.POST['med_id'], user=user_instance,
                                     specialty=request.POST['specialty'], specialty_desc=request.POST['specialty_desc'],
                                     province=request.POST['province'], address=request.POST['address'])
            med_service.save()

    return render(request, "login.html", {'errors': form.errors})


def login_page(request):
    return render(request, "login.html")


def auth(request):
    user = authenticate(
        username=request.POST['username'], password=request.POST['password'])

    if user is not None:
        login(request, user)
        print("Signed in")
    else:
        print("Not signed in")

    return redirect('users:login')


def profile(request, username):
    usr_info = User.objects.filter(username=username)[0]
    service = usr_info.service
    return render(request, "profile.html", {"usr_info": usr_info, "service": service})


def user_logout(request):
    logout(request)
    return redirect('users:login')

def edit_profile(request):
    username=request.user.username
    u = User.objects.filter(username=request.user.username)[0]
    try:
        if u:
            times = u.schedule.times.all()
        return render(request,'edit_profile.html', {'times': times, 'username': username})
    except:
        s = Schedule(med = u)
        s.save()
        
        return render(request,'edit_profile.html', {'times': [], 'username': username})


def create_time(request):
    username = request.POST.get('username')
    time = request.POST.get('time')
    u = User.objects.filter(username=username)[0]
    t = Time(time=time, schedule=u.schedule)
    t.save()
    data = {
        'time': t.time
    }
    return JsonResponse(data)