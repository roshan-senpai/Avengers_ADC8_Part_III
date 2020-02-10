from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from events.models import Event
import json

# create and read function using api
@csrf_exempt
def view_get_post_events(request):
    print("request: ",request.method)
    if request.method == "GET":
        events = Event.objects.all()
        list_of_events = list(events.values("event_name","venue"))
        dictionary_name = {
        "events":list_of_events
    }
        return JsonResponse(dictionary_name)
    elif request.method == "POST":
        print("body contents", request.body)
        print("Request type", type(request.body))
        python_dictionary_object = json.loads(request.body)
        print(python_dictionary_object['event_name'])
        Event.objects.create(event_name=python_dictionary_object['event_name'],venue=python_dictionary_object['venue'],event_date=python_dictionary_object['event_date'],manager=python_dictionary_object['manager'],)
        return JsonResponse({
            "message":"Successfully posted!!"
        })
    else:
        return HttpResponse("Other HTTP verbs testing")
        
# pagination
def view_events_pagination(request,pageno,size):
    if request.method=="GET":
        skip_first=size*(pageno-1)
        to=pageno*size
        event=Event.objects.values() [skip_first:to]
        dict={
            "event": list(event.values("event_name","venue"))
        }
        return JsonResponse(dict)


