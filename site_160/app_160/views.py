from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from . import forms

def index(request):
    return render(request, 'app_160/index.html')

@login_required()
def create_summary(request):
    if request.method == 'POST':
        form = forms.SummaryForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
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
