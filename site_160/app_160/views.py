from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms, models
from django.contrib.auth.signals import user_logged_in


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
            model.tags = form.cleaned_data['tags']
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
    return render(request, "app_160/logout.html")

def summary_list(request):
    summaries = models.SummaryModel.objects.all()
    return render(request, "app_160/list.html", context={"summaries": summaries})


def set_status_online(sender, user, request, **kwargs):
    print('User %s is logging in' % request.user.username)

user_logged_in.connect(set_status_online)
