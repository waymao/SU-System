from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import eventChangeForm, eventCreateForm
import datetime, base64, hashlib


def index(request):
    event_list = Event.objects.filter(time__gte=datetime.date.today()).order_by('time')
    return render(request, 'events/index.html', {'event_list': event_list})


def detailed(request, event_hash):
    event = get_object_or_404(Event, hash=event_hash)
    return render(request, 'events/detail.html', {'event': event})


def edit(request, event_hash):
    # if user does not have permission, refuse access.
    if not request.user.has_perm('events.can_add_event'):
        return render(request, 'permission_error.html')

    event = get_object_or_404(Event, hash=event_hash)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = eventChangeForm(request.POST)
        # check whether it's valid:
        if form1.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            event.date = form1.cleaned_data['time']
            event.save()
            return redirect("../")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = eventChangeForm()
        return render(request, 'events/edit.html', {'event': event, 'form': form})


def add_new(request):
    # if user does not have permission, refuse access.
    if not request.user.has_perm('events.can_add_event'):
        return render(request, 'permission_error.html')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = eventCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            event_name = form.cleaned_data['name']
            event_time = form.cleaned_data['time']
            event_type = form.cleaned_data['type']
            event_hash = base64.b64encode(hashlib.sha1(
                (event_name + event_time.strftime('%m-%d-%Y') + event_type).encode('utf-8')).digest()).decode('utf-8')[
                         0:11].replace("/", "_")
            Event.objects.create(name=event_name,
                                 time=event_time,
                                 description=form.cleaned_data['description'],
                                 type=event_type,
                                 publish_date=datetime.datetime.now(),
                                 is_private=0,
                                 hash=event_hash
                                 )
            return redirect("/events/" + event_hash + "/")
        else:
            return render(request, 'events/new.html', {'form': form})
    else:
        form = eventCreateForm()
        return render(request, 'events/new.html', {'form': form})

# Create your views here.
