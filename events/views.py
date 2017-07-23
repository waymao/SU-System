from django.shortcuts import render, get_object_or_404, redirect
from .models import Event
from .forms import eventChangeForm

def index(request):
    event_list = Event.objects.order_by('-date')
    return render(request, 'events/index.html', {'event_list': event_list})


def detailed(request, event_hash):
    event = get_object_or_404(Event, hash=event_hash)
    return render(request, 'events/detail.html', {'event': event})


def edit(request, event_hash):
    event = get_object_or_404(Event, hash=event_hash)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = eventChangeForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return redirect("../")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = eventChangeForm()
        return render(request, 'events/edit.html', {'event': event, 'form': form})

# Create your views here.
