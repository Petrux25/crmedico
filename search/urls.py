from django.urls import path
from . import views

app_name = 'search'
urlpatterns = [
    path('<int:page_number>', views.search, name="search"),
]
