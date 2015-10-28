from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import models
from serializers import CaloriesSerializer, StepsSerializer
from models import Calories,Steps
from rest_framework import permissions, routers, serializers, viewsets,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
# class base views a serilize that data
class CaloriesDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Calories resource. """
    queryset=Calories.objects.all()
    serializer_class=CaloriesSerializer
    
class StepsDetail(generics.RetrieveUpdateDestroyAPIView):
    """ Calories resource. """
    queryset=Steps.objects.all()
    serializer_class=StepsSerializer
    
class StepsViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Steps.objects.all()
    serializer_class = StepsSerializer
    
class CaloriesViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = Calories.objects.all()
    serializer_class = CaloriesSerializer
    
@api_view(['GET'])    
def get_calories_data(request, username=None):
    '''
    Process the data to pass it to the JS libraries to generate an SVG image
    '''
    
    mycalories = Calories.objects.filter(owner=1)


    chart_data = []

    for i in mycalories:
        chart_data.append({ 'calories': i.calories,
                            'dateAdded':i.dateAdded,
                        #   'owner': i.owner,
                           'unit': i.unit})

    # Return the results to the client
    return Response(chart_data)