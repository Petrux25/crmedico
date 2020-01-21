from django.shortcuts import render
from app_users.models import MedService


def search(request, page_number=1):
    first = (page_number - 1) * 10
    last = first + 10
    meds = list(map(mapUsers, MedService.objects.all()[first:last]))
    size = len(meds)
    return render(request, "search.html", {'meds': meds, 'size': size, 'page_number': page_number, 'next':page_number+1, 'prev':page_number-1})


def mapUsers(medServ):
    return medServ.user
