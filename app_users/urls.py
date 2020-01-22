from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('create/<usr_type>', views.create, name="create"),
    path('register/<usr_type>', views.register, name="register"),
    path('profile/<username>', views.profile, name="profile"),
    path('edit_profile/<username>', views.edit_profile, name="edit_profile"),
    path('login', views.login_page, name="login"),
    path('authenticate', views.auth, name="authenticate"),
]
