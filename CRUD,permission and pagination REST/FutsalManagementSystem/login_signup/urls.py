from django.contrib import admin
from .views import *
from django.urls import path

urlpatterns = [
    path('signup/',view_signup),
    path('login/',view_login_user),
    path('logout/',view_logout),
]