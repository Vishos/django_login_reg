from django.shortcuts import render, reverse, redirect
from ..login.models import User
from .models import Poke
# Create your views here.
def landing(request):
	context = {
		'all_users' : User.objects.all(),
		'all_pokes' : Poke.objects.all()
	}
	return render(request, 'dashboard/landing.html', context)

def createPoke(request):
	print request.POST['poke_receiver']
	Poke.objects.createPoke(
		sender=request.session['user_id'], 
		receiver=request.POST['poke_receiver'])
	return redirect('/dashboard')