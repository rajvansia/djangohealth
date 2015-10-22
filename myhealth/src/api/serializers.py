from rest_framework import serializers
import profiles
from profiles import models
from profiles.models import Profile,Myfamily
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.contrib.auth import get_user_model
# User = get_user_model()
# from django.contrib.auth.tools import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields = ('bio','gender','slug' )
        
class MyfamilySerializer(serializers.ModelSerializer):
    class Meta:
        model=Myfamily
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        # fields = ('url', 'username', 'email', 'is_staff')