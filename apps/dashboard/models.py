from __future__ import unicode_literals

from django.db import models
from ..login.models import User
# Create your models here.

class Poke(models.Model):
	poke_sender = models.ForeignKey(User, related_name="pokes_sent")
	poke_receiver = models.ForeignKey(User, related_name="pokes_received")
	count = models.IntegerField(default = 1)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)