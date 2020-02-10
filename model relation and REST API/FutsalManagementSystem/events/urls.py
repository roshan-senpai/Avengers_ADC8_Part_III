from django.contrib import admin
from django.urls import path
from .views import *
# url path for html pages
urlpatterns = [
    path('eventdataform/<int:ID>',view_eventform),
    path('eventdataform/update/<int:ID>',view_update_form_data_in_db),
    path('searchdata/<int:ID>',view_search_data)

]
