from django.contrib import admin
from django.urls import path, include
from app_users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_users.urls')),
    path('search/', include('search.urls'))
]
