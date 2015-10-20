from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
import datetime


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)
    is_parent = models.BooleanField(default=False)
    birthday=models.DateField(default=datetime.datetime.now)
    gender= models.CharField(max_length=30, blank=True,null=True)
    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
        
class Parent(models.Model):
    parent = models.ForeignKey(Profile,primary_key=True)
    def __str__(self):
        return "{}'s profile". format(self.parent)
class Child(models.Model):
    child = models.ForeignKey(Profile,primary_key=True)
    # def __unicode__(self):
    #     return u'%s %s' % (self.child)
    def __str__(self):
        return "{}'s profile". format(self.child)
class myid(models.Model):
    my_id = models.ForeignKey(Profile,primary_key=True)
    # def __unicode__(self):
    #     return u'%s %s' % (self.child)
    def __str__(self):
        return "{}'s profile". format(self.my_id)
class Family(models.Model):
    mychild = models.ForeignKey(Child)
    myparent = models.ForeignKey(Parent)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
    def __str__(self):
        return "{}'s profile". format(self.mychild)
        
class Myrolls(models.Model):
    roll= models.CharField(max_length=30, blank=True,null=True)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
    def __str__(self):
        return "{}'s profile". format(self.roll)
        
        
class Myfamily(models.Model):
    myself = models.ForeignKey(myid)
    myrelation = models.ForeignKey(Profile)
    thisroll= models.ForeignKey(Myrolls, blank=True,null=True)
    # def __unicode__(self):
    #     return u'%s %s' % (self.mychild, self.myparent)
#     # def __str__(self):
#     #     return "{}'s profile". format(self.)