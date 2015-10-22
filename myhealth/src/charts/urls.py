from django.conf.urls import url
from . import views
from django.conf.urls import patterns, url

urlpatterns = patterns('charts.views',
    # Examples:
    url(r'^$', 'home', name='home'),
    url(r'^piechart/', 'demo_piechart', name='demo_piechart'),
    url(r'^linechart/', 'demo_linechart', name='demo_linechart'),
     url(r'^linecharts/', 'demo_linechart_without_date', name='demo_linecharts'),
    )