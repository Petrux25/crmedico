from django.urls import path
from . import views

app_name = 'reservations'
urlpatterns = [
    path('create/<med_id>', views.create, name="create"),
    path("times", views.get_times, name="times"),
    path("save", views.save_appointment, name="save"),
]
