from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.

class PokeManager(models.Manager):
	def createPoke(self,sender, receiver):
		sender = User.objects.get(id=sender)
		receiver = User.objects.get(id=receiver)
		print "***********"
		print "inside pokeManager about to create a poke"
		print "************"
		existingPoke = Poke.objects.filter(poke_sender=sender, poke_receiver=receiver)
		if len(existingPoke) > 0:
			existingPoke[0].count += 1
			existingPoke[0].save()
		else:
			Poke.objects.create(poke_sender=sender, poke_receiver=receiver)
		return "done"
    	

class Poke(models.Model):
	poke_sender = models.ForeignKey(User, related_name="pokes_sent")
	poke_receiver = models.ForeignKey(User, related_name="pokes_received")
	count = models.IntegerField(default = 1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = PokeManager()