from django.shortcuts import render, redirect
from .forms import UserForm
from .models import MedService, UserRoles, UserPhones
from django.contrib.auth.models import User
from django.core import serializers


def register(request, usr_type):
    specialties = MedService.SPECIALTIES
    provinces = MedService.PROVINCES
    return render(request, "register.html", {'usr_type': usr_type, 'specialties': specialties, 'provinces': provinces})


def create(request, usr_type):
    is_user_med = (usr_type == "med")
    user_role = 2 if is_user_med else 1
    form = UserForm(request.POST)
    if form.is_valid():
        user_instance = form.save()
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


def profile(request):
    usr = getUsrInfo("305060162")
    print(usr)
    return render(request, "profile.html")

def getUsrInfo(id):
    usr=User.objects.filter(username=id)[0]
    usr = {'username':usr.username, 'first_name':usr.first_name, 'last_name':usr.last_name,'email':usr.email, 'phone':usr.phone.phone, "role":usr.role.role}
    return usr

