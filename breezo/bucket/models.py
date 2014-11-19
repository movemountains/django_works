import datetime

from django.db import models
from django.utils.encoding import smart_unicode
from django.utils import timezone

# Create your models here.

class BucketList(models.Model):
    Public = 'P'
    Private = 'R'
    OPTION = (
        ('P','Public'),
        ('R','Private'),
)    

   #user_email=models.EmailField()
    bucket_name=models.CharField(max_length=120, null=True, blank=True)
    user_email=models.EmailField() 
    bucket_description=models.CharField(max_length=150, null=True, blank=True)
    bucket_open_date=models.DateTimeField('date started', blank=True)
    bucket_option = models.CharField(max_length=1, choices=OPTION,default='P')

class To_Do(models.Model):
    card_name=models.CharField(max_length=400, null=True, blank=True)
    dead_line=models.DateTimeField('deadline date', blank=True)

class Done(models.Model):
    card_name=models.CharField(max_length=400, null=True, blank=True)  
    done_date=models.DateTimeField('Finished date', blank=True) 

class Doing(models.Model):
    card_name=models.CharField(max_length=400, null=True, blank=True)
    doing_date=models.DateTimeField('starting date', blank=True)


class Meta:
    ordering =['bucket_name']

