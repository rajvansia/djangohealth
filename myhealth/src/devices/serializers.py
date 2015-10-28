from rest_framework import serializers
from django.db import models
from models import Devices



class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Devices
        
     

