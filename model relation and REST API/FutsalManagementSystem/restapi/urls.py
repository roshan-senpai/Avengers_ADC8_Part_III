from django.urls import path
from .views import *

urlpatterns = [
    path('events/',view_get_post_events),
    path('events/<int:ID>',view_getByID_updateByID_deleteByID),
] 