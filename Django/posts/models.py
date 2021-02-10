"""posts models
"""
#django
from django.db import models
from django.db.models.fields import AutoField

class User(models.Model):
    id = models.UUIDField(primary_key=True)

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)
    
    firstName = models.CharField(max_length=50)
    lasName = models.CharField(max_length=50)
    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)



