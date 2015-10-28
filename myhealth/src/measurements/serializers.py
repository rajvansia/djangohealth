from rest_framework import serializers
from django.db import models
from models import Steps,Calories



class StepsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Steps
        
class CaloriesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Calories
        

     

