from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import api.urls
import accounts.urls
import charts.urls
from . import views
from django.contrib.auth.models import  Group
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib import admin
admin.autodiscover()
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, TokenHasScope
from measurements import measurementsviews
from measurements.measurementsviews import StepsViewSet, CaloriesViewSet
# from oauth2.provider.views.mixins import ScopedResourceMixin

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ['groups']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
# Routers provide an easy way of automatically determining the URL conf

router = routers.DefaultRouter()
router.register(r'users', UserViewSet,base_name='users')
router.register(r'groups', GroupViewSet,base_name='groups')
router.register(r'steps', StepsViewSet,base_name='steps')
router.register(r'calories', CaloriesViewSet,base_name='calories')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chart/', include(charts.urls, namespace='charts')),
    url(r'^api/', include(api.urls, namespace='api')),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),

]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
