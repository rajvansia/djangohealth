from __future__ import unicode_literals
from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from braces.views import LoginRequiredMixin
from . import forms
from . import models
from serializers import ProfileSerializer
from models import Child,Parent,Profile,Family
from rest_framework import generics, permissions
# class base views a serilize that data
class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer



class ShowProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/show_profile.html"
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        # if slug:
        #     profile = get_object_or_404(models.Profile, slug=slug)
        #     user = profile.user
        # else:
        # prevents te slug from accessing the user who is them
        user = self.request.user
        
        # child=Child.objects.get(pk=1)

        if user == self.request.user:
            mypk=user.profile.user_id
            # child=Child.objects.get(pk=mypk)
            parent=Parent.objects.get(pk=mypk)
            myfamily=Family.objects.get(pk=3)
            mychildren=parent.family_set.all()
            kwargs["editable"] = True
        kwargs["show_user"] = user
        # kwargs["show_child"] = child
        kwargs["show_children"] = mychildren
        kwargs["show_family"] = myfamily
        return super(ShowProfile, self).get(request, *args, **kwargs)


class EditProfile(LoginRequiredMixin, generic.TemplateView):
    template_name = "profiles/edit_profile.html"
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        user = self.request.user
        if "user_form" not in kwargs:
            kwargs["user_form"] = forms.UserForm(instance=user)
        if "profile_form" not in kwargs:
            kwargs["profile_form"] = forms.ProfileForm(instance=user.profile)
        return super(EditProfile, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = forms.UserForm(request.POST, instance=user)
        profile_form = forms.ProfileForm(request.POST,
                                         request.FILES,
                                         instance=user.profile)
        if not (user_form.is_valid() and profile_form.is_valid()):
            messages.error(request, "There was a problem with the form. "
                           "Please check the details.")
            user_form = forms.UserForm(instance=user)
            profile_form = forms.ProfileForm(instance=user.profile)
            return super(EditProfile, self).get(request,
                                                user_form=user_form,
                                                profile_form=profile_form)
        # Both forms are fine. Time to save!
        user_form.save()
        profile = profile_form.save(commit=False)
        profile.user = user
        profile.save()
        messages.success(request, "Profile details saved!")
        return redirect("profiles:show_self")
