from django.contrib import admin
from django.urls import path

import accounts.views

urlpatterns = [
    path("register/", accounts.views.register_request, name="register"),
    path("login/", accounts.views.login_request, name="login"),
    path("logout/", accounts.views.logout_request, name= "logout")
]