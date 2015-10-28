from rest_framework import serializers
from django.db import models
from models import Tasks



class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tasks
        