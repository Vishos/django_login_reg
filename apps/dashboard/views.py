from django.shortcuts import render, reverse, redirect
from ..login.models import User
# Create your views here.
def landing(request):
	context = {
		'all_users' : User.objects.all()
	}
	return render(request, 'dashboard/landing.html', context)

def createPoke(request):
	print request.POST['poke_receiver']
	return redirect('/dashboard')