from __future__ import unicode_literals
from django.contrib import admin
from authtools.admin import NamedUserAdmin
from .models import Profile, Child, Family, Parent,myid,Myfamily,Myrolls
from django.contrib.auth import get_user_model
from django.core.urlresolvers import reverse
from devices.models import Devices
from tasks.models import Tasks
from measurements.models import Steps, Calories 

class StepsAdmin(admin.ModelAdmin):
  list_display=('owner','deviceId','steps','unit','dateAdded')
  search_feilds=('dateAdded','owner')
admin.site.register(Steps,StepsAdmin)

class DevicesAdmin(admin.ModelAdmin):
  list_display=('owner','deviceType')
  search_feilds=('deviceType','owner')
admin.site.register(Devices,DevicesAdmin)

class CaloriesAdmin(admin.ModelAdmin):
  list_display=('owner','deviceId','calories','unit','dateAdded')
  search_feilds=('dateAdded','owner')
admin.site.register(Calories,CaloriesAdmin)

class TasksAdmin(admin.ModelAdmin):
  list_display=('owner','tasksType')
  search_feilds=('tasksType','owner')
admin.site.register(Tasks,TasksAdmin)

class ParentAdmin(admin.ModelAdmin):
  list_display=('parent',)
  search_feilds=('name')
admin.site.register(Parent,ParentAdmin)
class MyrollsAdmin(admin.ModelAdmin):
  list_display=('roll',)
  search_feilds=('roll')
admin.site.register(Myrolls,MyrollsAdmin)
class MyfamilyAdmin(admin.ModelAdmin):
  list_display=('myself','myrelation','thisroll')
  search_feilds=('myself',)
admin.site.register(Myfamily,MyfamilyAdmin)

class FamilyAdmin(admin.ModelAdmin):
  list_display=('id','mychild','myparent')
  search_feilds=('mychild',"myparent")
admin.site.register(Family,FamilyAdmin)
class myidAdmin(admin.ModelAdmin):
  list_display=('my_id',)
  search_feilds=('id','my_id')
admin.site.register(myid,myidAdmin)

class ChildAdmin(admin.ModelAdmin):
  list_display=('child',)
  search_feilds=('name')
admin.site.register(Child,ChildAdmin)

User = get_user_model()


class UserProfileInline(admin.StackedInline):
    model = Profile


class NewUserAdmin(NamedUserAdmin):
    inlines = [UserProfileInline]
    list_display = ('is_active', 'email', 'name', 'permalink',
                    'is_superuser', 'is_staff',)

    # 'View on site' didn't work since the original User model needs to
    # have get_absolute_url defined. So showing on the list display
    # was a workaround.
    def permalink(self, obj):
        url = reverse("profiles:show",
                      kwargs={"slug": obj.profile.slug})
        # Unicode hex b6 is the Pilcrow sign
        return '<a href="{}">{}</a>'.format(url, '\xb6')
    permalink.allow_tags = True

admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)
