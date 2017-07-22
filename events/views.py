from django.shortcuts import render, get_object_or_404
from .models import Event


def index(request):
    event_list = Event.objects.order_by('-date')
    return render(request, 'events/index.html', {'event_list': event_list})


def detailed(request,event_hash):
    event = get_object_or_404(Event, hash=event_hash)
    return render(request, 'events/detail.html', {'event': event})

# Create your views here.
