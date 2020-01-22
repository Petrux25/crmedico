from django.contrib import admin
from django.urls import path, include
from app_users import views as app_users_views
from search import views
from reservations import views


urlpatterns = [
    path('', app_users_views.login_page),
    path('admin/', admin.site.urls),
    path('users/', include('app_users.urls')),
    path('search/', include('search.urls'), name="search"),
    path('reservations/', include('reservations.urls'), name="reservations"),
]
