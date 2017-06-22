from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'app_160/index.html')

@login_required()
def create_summary(request):
    return render(request, 'app_160/create_summary.html', context={"user": request.user})

def login(request):
    current_user = request.user
    print(current_user)
    return render(request, "app_160/login.html", context={"user": current_user})
