from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from events.models import *
import json

@csrf_exempt
def view_get_post_events(request):
        #get event list
    if request.method == "GET":
        events = Event.objects.all()
        list_of_event = list(events.values("event_name","venue","event_date","manager"))
        print("List of Event objects => ",list_of_event)
        dictionary_name = {
        "events":list_of_event
    }
        return JsonResponse(dictionary_name)

    elif request.method == "POST":
        #post event
        python_dictionary_object = json.loads(request.body)
        Event.objects.create(event_name=python_dictionary_object['event_name'],venue=python_dictionary_object['venue'],event_date=python_dictionary_object['event_date'],manager=python_dictionary_object['manager'],)
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")

@csrf_exempt
def view_getByID_updateByID_deleteByID(request,ID):
    #get by id
    if request.method == "GET":
        events = Event.objects.get(id = ID)
        return JsonResponse({
            "id":events.id,
            "name of event":events.event_name,
            "venue":events.venue,
            "date of event":events.event_date,
            "name of manager":events.manager
        })
        #update data in events
    elif request.method == "PUT":
        event = Event.objects.get(id=ID)
        python_dictionary_object = json.loads(request.body)
        event.event_name = python_dictionary_object['event_name']
        event.venue = python_dictionary_object['venue']
        event.event_date = python_dictionary_object['event_date']
        event.manager = python_dictionary_object['manager']
        event.save()        
        return JsonResponse({
            "Message":"Updated successfully!!"
        })
        #delete by id
    elif request.method == "DELETE":
        event=Event.objects.get(id=ID)
        event.delete()
        return JsonResponse({
            "message":" Delete Successfully!!"
        })

    else:
        return JsonResponse({
            "message":" Other http verbs Testing"
        }) 