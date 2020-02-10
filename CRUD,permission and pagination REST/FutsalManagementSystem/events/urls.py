from django.contrib import admin
from django.urls import path
from .views import *
from django.shortcuts import render,redirect
urlpatterns=[
    path('viewevent/',view_event_data,name='home'),
    path('eventform/',view_event_form1, name='form'),
    path('eventform/save',view_event_save),
    path('viewevent/delete/<int:ID>',view_event_delete),
    path('viewevent/',get_isauthenticated_welcome),
    path('eventdataform/<int:ID>',view_event_form),
    path('update/<int:ID>',view_update_data),
    path('searchdata/',view_search_data),
    path('home/',view_home_page)

]
