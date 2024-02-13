from django.shortcuts import render,redirect
from accounts.forms import UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import CustomUser
from events.models import Event , EventRegistration
from events.forms import CreateEventForm 
from datetime import datetime ,date
from django.http import JsonResponse

###  My  Events
@login_required(login_url="accounts:user-login")
def my_events(request):
    events = Event.objects.filter(organizer=request.user)
    return render(
                request , 
                "events/my-events.html" , 
                locals()  
                )


@login_required(login_url="accounts:user-login")
def add_event(request):
    if request.POST:
        form = CreateEventForm(request.POST , request.FILES )
        if form.is_valid():
            obj=form.save(commit=False)
            obj.organizer = request.user
            obj.save()

            messages.success(request ,"Event Added Successfully")
            return redirect("events:my-events")
        else:
            return render(request , "events/add-event.html" , {'form':form})
    form = CreateEventForm()
    return render(request , "events/add-event.html" , locals())


@login_required(login_url="accounts:user-login")
def update_event(request,pk):
    obj=Event.objects.get(id=pk)
    if request.POST:
        form = CreateEventForm(request.POST , request.FILES , instance=obj )
        if form.is_valid():
            form.save()
            messages.success(request ,"Event Updated Successfully")
            return redirect("events:my-events")
        else:
            return render(request , "events/add-event.html" ,{'form':form} )
    
    form = CreateEventForm(instance=obj)
    return render(request , "events/add-event.html" , locals())


############  Other Events 
@login_required(login_url="accounts:user-login")
def other_events(request):
    events = Event.objects.filter(registration_deadline__gte = date.today()).exclude(organizer=request.user)
    
    return render(
                request , 
                "events/other-events.html" , 
                locals()  
                )


@login_required(login_url="accounts:user-login")
def event_view(request,pk):
    event=Event.objects.get(id=pk)
    return render(request , "events/event-view.html" , locals())


@login_required(login_url="accounts:user-login")
def paticipents_view(request,pk):
    event = Event.objects.get(id=pk)
    participants=EventRegistration.objects.filter(event=event)
    return render(request , "events/participants-view.html" , locals())

def event_registration(request):
    query=request.GET.get("query")
    event_id=request.GET.get("event_id")
    
    if query == "yes":

        event=Event.objects.get(id=event_id)
        
        if EventRegistration.objects.filter(user = request.user , event = event ).exists():
            return JsonResponse({'status': "You are already Registerd! Sir "} )
        
        EventRegistration.objects.create(
            event = event ,
            user = request.user
        )
        messages.success(request , "Your Registrtaion is Successfull Will connnect With You soon")
        return JsonResponse({'status': "success"} )
    else:
        return JsonResponse({'status': "something went wrong contact admin"} )    