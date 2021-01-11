from django.forms import ModelForm
from django import forms
# from accounts.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']
# class UserProfileInfoForm(ModelForm):
#      class Meta:
#          model = UserProfileInfo
#          fields = ['portfolio_site','profile_pic']