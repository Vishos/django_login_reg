from __future__ import unicode_literals
from datetime import datetime
from django.db import models

# Create your models here.

class UserManager(models.Manager):
    def register(self, postData):
        errors = {}
        response = {
            'status' : True,
        }
        if len(postData['first_name']) < 3:
            errors['first_name'] = "First Name must be at least 3 characters"
        if len(postData['email']) < 3:
            errors['email'] = "email needs to be supplied"
        else:
            existing = User.objects.filter(email = postData['email'].lower())
            if len(existing) > 0:
                print 'the email validation is working'
                errors['email'] = 'that email is already taken'
                    
        if len(errors) > 0:
            response['errors'] = errors
            response['status'] = False
        else:
            response['user'] = User.objects.create(
                first_name = postData['first_name'], 
                last_name = postData['last_name'], 
                email = postData['email'], 
                password = postData['password'])

        return response

    def login(self, postData):
        response = {
            'status' : False,
            'errors' : {'login' : 'incorect email / password'}
        }
        existing = self.filter(email=postData['email'])
        if len(existing) > 0:
            if postData['password'] == existing[0].password:
                response['user']=existing[0]
                response['status'] = True

        return response
            

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


