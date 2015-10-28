from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import datetime
from profiles.models import Profile
from devices.models import Devices

class Steps(models.Model):
    owner= models.ForeignKey(Profile,null=True)
    deviceId= models.ForeignKey(Devices,null=True)
    steps=models.DecimalField(max_digits=13, decimal_places = 8, null=True, blank=True) 
    unit=models.CharField(max_length=30, blank=True,null=True)
    dateAdded=models.DateField(default=datetime.datetime.now)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
    def __str__(self):
        return "{} Steps". format(self.dateAdded)
        
class Calories(models.Model):
    owner= models.ForeignKey(Profile,null=True)
    deviceId= models.ForeignKey(Devices,null=True)
    calories=models.DecimalField(max_digits=13, decimal_places = 8, null=True, blank=True) 
    unit=models.CharField(max_length=30, blank=True,null=True)
    dateAdded=models.DateField(default=datetime.datetime.now)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
    def __str__(self):
        return "{} Calories". format(self.dateAdded)       