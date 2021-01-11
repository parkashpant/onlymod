from django.forms import ModelForm
from django import forms
from modprofile.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileInfoForm(ModelForm):
     class Meta:
         model = UserProfileInfo
         fields = ['year_of_exp','work_domain', 'linkedin_url', 'profile_pic']