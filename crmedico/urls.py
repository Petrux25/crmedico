from django.contrib import admin
from django.urls import path, include
from app_users import views
from search import views
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('search/', include('search.urls'), name="search"),
    path('reservations/', include('reservations.urls'), name="reservations"),
]
