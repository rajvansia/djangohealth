from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import models
from serializers import DevicesSerializer
from models import Devices
from rest_framework import generics, permissions
# class base views a serilize that data
class DevicesDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Device resource. """
    queryset=Devices.objects.all()
    serializer_class=DevicesSerializer