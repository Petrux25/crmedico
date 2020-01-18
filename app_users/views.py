from django.shortcuts import render, redirect
from .forms import UserForm
from .models import MedService, UserRoles
from django.contrib.auth.models import User


def register(request, usr_type):
    specialties = MedService.SPECIALTIES
    return render(request, "register.html", {'usr_type': usr_type, 'specialties': specialties})


def create(request, usr_type):
    is_user_med = usr_type == "med"
    user_role = 2 if is_user_med else 1
    form = UserForm(request.POST)
    if form.is_valid():
        user_instance = form.save()
        role_instance = UserRoles(user=user_instance, role=user_role)
        role_instance.save()

        if is_user_med:
            med_service = MedService(med_id=request.POST['med_id'], user=user_instance,
                                     specialty=request.POST['specialty'], specialty_desc=request.POST['specialty_desc'])
            med_service.save()

    return render(request, "login.html", {'errors': form.errors})


def login(request):
    return render(request, "login.html")


def auth(request):
    can_login = log_usr(request.POST['username'], request.POST['password'])
    if can_login:
        print("Signed in")
    else:
        print("Not signed in")

    return redirect('login')


def log_usr(username, password):
    return User.objects.filter(username=username, password=password).exists()
