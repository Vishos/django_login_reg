from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import User
# Create your views here.
def index(request):
    return render(request, "login/index.html", {'status':True})

def processReg(request):
    response = User.objects.register(request.POST)
    if not response['status']:
        return render(request, "login/index.html", response)
    request.session['user_id']=response['user'].id
    return redirect('/success')

def processLog(request):
    response = User.objects.login(request.POST)
    if not response['status']:
        return render(request, 'login/index.html', response)
    
    request.session['user_id']=response['user'].id
    
    return redirect('/success')

def success(request):
    return render(request, 'login/success.html')


def logout(request):
    request.session.flush()
    return redirect('/')