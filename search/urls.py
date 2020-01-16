from django.urls import path
from . import views

urlpatterns = [
    path('<int:page_number>', views.search, name="search"),
]
