from django.urls import path
from .views import *

urlpatterns = [
    path('events/',view_get_post_events),
    path('events/<int:pageno>/<int:size>/',view_events_pagination)
]