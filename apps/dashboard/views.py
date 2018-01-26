from django.shortcuts import render, reverse, redirect
from ..login.models import User
# Create your views here.
def landing(request):
    users = User.objects.all()
    return render(request, 'dashboard/landing.html', {'users':users})