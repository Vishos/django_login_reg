from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, "login/index.html", {'status':True})

def processReg(request):
    confirm = request.POST['confirm']
    response = User.objects.validate(request.POST)
    if not response['status']:
        return render(request, "login/index.html", response)
    return redirect(reverse('dashboard:landing'))