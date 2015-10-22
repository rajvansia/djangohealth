from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #   url(r'^$', 'band.views.all_bands'),
      url(r'^profiles/(?P<pk>[0-9])/$',  views.ProfileDetail.as_view()),
    #   url(r'^api/(?P<pk>[0-9]+)/$', views.BandDetail.as_view()),
      url(r'^familes/(?P<pk>[0-9])/$',  views.MyfamilyDetail.as_view()),
      url(r'^users/(?P<pk>[0-9])/$',  views.UserDetail.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])
