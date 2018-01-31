from django.shortcuts import render, reverse, redirect
from ..login.models import User
from django.db.models import Sum
from .models import Poke
# Create your views here.
def landing(request):
    	user = User.objects.get(id=request.session['user_id'])
	context = {
		'session_user' : user,
		'all_users' : User.objects.exclude(id=request.session['user_id']).annotate(num_pokes=Sum('pokes_received__count')),
		'all_pokes' : Poke.objects.all(),
		'frienemies': Poke.objects.filter(poke_receiver=user).order_by("-count")
	}
	return render(request, 'dashboard/landing.html', context)

def createPoke(request):
	print request.POST['poke_receiver']
	Poke.objects.createPoke(
		sender=request.session['user_id'], 
		receiver=request.POST['poke_receiver'])
	return redirect('/dashboard')