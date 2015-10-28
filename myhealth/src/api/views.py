from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import models
from serializers import ProfileSerializer,MyfamilySerializer,UserSerializer
from profiles.models import Profile, Myfamily
from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
User = get_user_model()
# from django.contrib.authtools import User
# Create your views here.
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Profile resource. """
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    
class MyfamilyDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Myfamily resource. """
    queryset=Myfamily.objects.all()
    serializer_class=MyfamilySerializer
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    """ User resource. """
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]