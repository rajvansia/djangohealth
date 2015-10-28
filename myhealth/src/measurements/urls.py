from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import permissions, routers, serializers, viewsets
from measurements import measurementsviews
from measurementsviews import StepsViewSet ,get_calories_data

 
# router = routers.DefaultRouter()
# router.register(r'^allsteps', StepsViewSet)
# urlpatterns=[
    
#      url(r'^', include(router.urls)),
#     ]

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #   url(r'^$', 'band.views.all_bands'),
 
        url(r'^Calories/(?P<pk>[0-9])/$',  measurementsviews.CaloriesDetail.as_view()),
        url(r'^Steps/(?P<pk>[0-9])/$',  measurementsviews.StepsDetail.as_view()),
        url(r'^allsteps/$',  measurementsviews.StepsViewSet),
        url(r'^caloriesdata/$', # JS
        measurementsviews.get_calories_data,
        name='caloriesdata'),
    
)

# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
