from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    