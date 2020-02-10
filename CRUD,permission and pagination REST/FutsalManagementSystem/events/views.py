from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Event
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission

# Create your views here.
def view_home_page(request):
    return render(request,'event/index.html')

# view function for reading events from database
def view_event_data(request):
    events_list=Event.objects.all()
    con_var={
        'events':events_list
    }
    return render(request,'event/viewevent.html',con_var)

# for register event page
def view_event_form1(request):
    return render(request,'event/save_event.html')

# view function for registering event
def view_event_save(request):
    if request.method == "POST":
        get_name=request.POST['event_name']
        get_venue=request.POST['event_venue']
        get_date=request.POST['event_date']
        get_manager=request.POST['event_manager']
        #get_files=request.POST['files']
        Event.objects.create(event_name=get_name,venue=get_venue,event_date=get_date,manager=get_manager)
        return HttpResponse("Added Sucessfully")    
    else:
        return HttpResponse("Error while adding") 

# view function for deleting event
def view_event_delete(request,ID):
    print(ID)
    event_obj=Event.objects.get(id=ID)
    con_var={
        'event':event_obj
    }
    event_obj.delete()
    return render(request,'event/delete_data.html',con_var)

# for authentication   
def get_isauthenticated_welcome(request):
    if request.user.is_authenticated:
        return render(request,"event/viewevent.html")
    else:
        return HttpResponse('Please login first')

# view function for updating page
def view_update_page(request):
    return render(request,'event/update.html')

# view function for listing event data page
def view_event_form(request,ID):
    print(ID)
    event_obj = Event.objects.get(id=ID)

    context_varible = {
        'event':event_obj
    }
    return render(request,'event/eventdataupdateform.html',context_varible)

# view function for updating in the database page
def view_update_data(request,ID):
    event_obj = Event.objects.get(id=ID)
    event_form_data = request.POST
    print(event_form_data)
    event_obj.event_name = request.POST['event_name']
    event_obj.venue =request.POST['venue']
    event_obj.event_date = request.POST['event_date']
    event_obj.manager = request.POST['manager']
    event_obj.save()
    return HttpResponse("Record Updated!!")


# view function for searhing in the database page
def view_search_data(request):
    if request.method=='POST':
        search=request.POST['srh']
        if search:
            match=Event.objects.filter(event_name__icontains=search)

            if match:
                return render(request,'event/search.html',{'sr':match})

            else:
                return HttpResponse('NO EVENT FOUND!')
                       
        else:
            return HttpResponse('ENTER EVENT NAME!!')

    else:
        return render(request,'event/searchdata.html')