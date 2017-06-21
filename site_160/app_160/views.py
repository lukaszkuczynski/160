from django.shortcuts import render

def index(request):
    return render(request, 'app_160/index.html')

def create_summary(request):
    return render(request, 'app_160/create_summary.html')
