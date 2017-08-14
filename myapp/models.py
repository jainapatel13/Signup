from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class Details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    Mobile=models.IntegerField(null=True,blank=True)
    image_path = models.ImageField(upload_to='',null=True,blank=True)
def __str__(self):
    return self.user