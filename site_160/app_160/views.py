from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from . import forms, models
from django.contrib.auth.signals import user_logged_in
from django.core import serializers


def index(request):
    return render(request, 'app_160/index.html')

@login_required()
def create_summary(request):
    if request.method == 'POST':
        form = forms.SummaryForm(request.POST)
        if form.is_valid():
            model = models.SummaryModel()
            model.author = request.user.username
            model.url = form.cleaned_data['url']
            model.text = form.cleaned_data['text']
            model.tags = form.cleaned_data['tags'].split(',')
            model.save()
            return HttpResponseRedirect('/created/')
    else:
        form = forms.SummaryForm()
    return render(request, 'app_160/create_summary.html', context={"user": request.user, "form": form})

def summary_created(request):
    return render(request, "app_160/summary_created.html")

def login(request):
    return render(request, "app_160/login.html", context={"user": request.user})

def oauth_logout(request):
    new_event('User logging out', request, 'access')
    return render(request, "app_160/logout.html")

def summary_list(request):
    summaries = models.SummaryModel.objects.all().order_by('-created_at')
    return render(request, "app_160/list.html", context={"summaries": summaries})

def new_event(description, request, event_type=''):
    event = models.Event()
    event.description = description
    event.user = request.user.username
    event.event_type = event_type
    event.save()

def set_status_online(sender, user, request, **kwargs):
    new_event(description='User logging in', request=request, event_type='access')

def redirect(request):
    if request.method == 'GET':
        url_to_redirect = request.GET['next_url']
        print(url_to_redirect)
        new_event('Redirecting to %s' % url_to_redirect, request, 'redirect')
        return HttpResponseRedirect(url_to_redirect)

@login_required()
@permission_required('is_superuser')
def events(request):
    event_objects = models.Event.objects.all().order_by('-timestamp')
    return render(request, "app_160/events.html", context={"events": event_objects})

user_logged_in.connect(set_status_online)
