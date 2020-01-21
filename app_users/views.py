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
    usr = User.objects.filter(username="305060162")[0]
    usr_info = buildUsrInfo(usr)
    service = buildMedService(usr)

    return render(request, "profile.html", {"usr_info": usr_info, "service": service})


def buildUsrInfo(usr):
    role = usr.role.role
    usr = {'username': usr.username, 'first_name': usr.first_name, 'last_name': usr.last_name,
           'email': usr.email, 'phone': usr.phone.phone, "role": role, "role_desc": getTupleVal(UserRoles.ROLES, role)}
    return usr


def buildMedService(usr):
    serv = usr.service
    med_service = {"med_id": serv.med_id,
                   "med_abbv": usr.last_name.split(' ')[0],
                   "specialty": getTupleVal(MedService.SPECIALTIES, serv.specialty),
                   "specialty_desc": serv.specialty_desc,
                   "province": getTupleVal(MedService.PROVINCES, serv.province),
                   "address": serv.address
                   }
    return med_service


def getTupleVal(tup, index):
    return tup[index-1][1]
