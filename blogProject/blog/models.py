from django.db import models
from django.contrib import admin
from django.contrib.sites.models import Site

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, primary_key=True)

    def __str__(self): # __uinicode__
        return self.email

