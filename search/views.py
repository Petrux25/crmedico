from django.shortcuts import render
from app_users.models import MedService

def search(request):
    specialties = MedService.SPECIALTIES
    provinces = MedService.PROVINCES
    return render(request, "search.html", {'specialties': specialties, 'provinces': provinces})

def result(request, page_number=1):
    all_meds = MedService.objects.all()
    description = request.GET['description']
    province = request.GET['province']
    specialty = request.GET['specialty']
    variables = {'specialty_desc__contains': description, 'province': province, 'specialty':specialty}
    arguments = {}
    for k, v in variables.items():
        if v:
            arguments[k] = v
    all_meds = all_meds.filter(**arguments)
    first = (page_number - 1) * 10
    last = first + 10
    meds = list(map(mapUsers, all_meds[first:last]))
    size = len(meds)
    return render(request, "result.html", {'meds': meds, 'size': size, 'page_number': page_number, 'next':page_number+1, 'prev':page_number-1})


def mapUsers(medServ):
    return medServ.user
