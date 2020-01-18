from django.shortcuts import render
# from app_users.models import MedicalUser
# def search(request, page_number = 1):
#     first = (page_number - 1) * 10
#     last = first + 10
#     meds = MedicalUser.objects.all()[first:last]
#     size = len(meds)
#     return render(request, "search.html", {'meds':meds, 'size':size, 'page_number':page_number})
