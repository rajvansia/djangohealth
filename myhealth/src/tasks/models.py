from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import datetime
from profiles.models import Profile

class Tasks(models.Model):
    owner= models.ForeignKey(Profile,null=True)
    tasksType=models.CharField(max_length=30, blank=True,null=True)
    dateAdded=models.DateField(default=datetime.datetime.now)
    tasksDetail=models.CharField(max_length=30, blank=True,null=True)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
    def __str__(self):
        return "{} device". format(self.tasksType)
        
        