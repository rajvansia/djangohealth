from rest_framework import serializers
from django.db import models
from models import Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        
        def get_status_display(self, obj):
           return obj.get_status_display()




# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.HyperlinkedIdentityField('posts', view_name='userpost-list', lookup_field='username')

#     class Meta:
#         model = User
#         # fields = ('id', 'username', 'first_name', 'last_name', 'posts', )