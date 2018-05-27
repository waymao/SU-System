from django.shortcuts import render, get_object_or_404, redirect
from .models import Club, MemberInfo
from .forms import clubChangeForm, clubCreateForm
import datetime
import base64
import hashlib


def get_current_year():
    if datetime.datetime.today().month > 7:
        current_year = datetime.date.today().year
    else:
        current_year = datetime.date.today().year - 1
    return current_year


def index(request):
    current_year = get_current_year()
    club_list = Club.objects.filter(year=current_year).order_by('name')
    return render(request, 'clubs/index.html', {'club_list': club_list})


def detailed(request, club_hash):
    club = get_object_or_404(Club, hash=club_hash)
    member_list = MemberInfo.objects.filter(ApprovalStatus='AP', club_ref=club)
    return render(request, 'clubs/detail.html', {'club': club, "member_list": member_list})


def edit(request, club_hash):
    # if user does not have permission, refuse access.
    if not request.user.has_perm('Clubs.can_add_Club'):
        return render(request, 'permission_error.html')

    club = get_object_or_404(Club, hash=club_hash)
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form1 = clubChangeForm(request.POST)
        # check whether it's valid:
        if form1.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            club.description = form1.cleaned_data['description']
            club.save()
            return redirect("../")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = clubChangeForm(initial={'description': club.description})
        return render(request, 'clubs/edit.html', {'club': club, 'form': form})


def add_new(request):
    CLUB_CURRENT_YEAR = str(get_current_year())
    # if user does not have permission, refuse access.
    if not request.user.has_perm('Clubs.can_add_Club'):
        return render(request, 'permission_error.html')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = clubCreateForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            club_name = form.cleaned_data['name']

            club_type = "normal"
            club_hash = base64.b64encode(hashlib.sha1(
                (club_name + CLUB_CURRENT_YEAR + club_type).encode('utf-8')).digest()).decode('utf-8')[
                        0:11].replace("/", "_")
            Club.objects.create(name=club_name,
                                year=CLUB_CURRENT_YEAR,
                                description=form.cleaned_data['description'],
                                type=club_type,
                                publish_date=datetime.datetime.now(),
                                hash=club_hash
                                )
            return redirect("/clubs/" + club_hash + "/")
        else:
            return render(request, 'clubs/new.html', {'form': form, 'club_current_year': CLUB_CURRENT_YEAR})
    else:
        form = clubCreateForm()
        return render(request, 'clubs/new.html', {'form': form, 'club_current_year': CLUB_CURRENT_YEAR})


def history(request):
    club_list = Club.objects.filter(time__lte=datetime.date.today()).order_by('-time')
    return render(request, 'clubs/history.html', {'club_list': club_list})

# Create your views here.
