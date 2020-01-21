from django.urls import path
from . import views

urlpatterns = [
    path('create/<usr_type>', views.create, name="create"),
    path('register/<usr_type>', views.register, name="register"),
    path('login', views.login, name="login"),
    path('auth', views.auth, name="auth"),
    path('profile', views.profile, name="profile")
]
