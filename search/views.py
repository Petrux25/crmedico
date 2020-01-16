from django.shortcuts import render
from app_users.models import MedicalUser
def search(request):
    meds = MedicalUser.objects.all
    return render(request, "search.html", {'meds':meds})