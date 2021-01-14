from django.forms import ModelForm
from django import forms
from userprofile.models import UserProfileInfo
from django.contrib.auth.models import User

class UserProfileInfoForm(ModelForm):
     class Meta:
         model = UserProfileInfo
         fields = ['year_of_exp','work_domain', 'linkedin_url', 'profile_pic']


class UserChangeForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email']

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        f = self.fields.get('user_permissions', None)
        if f is not None:
            f.queryset = f.queryset.select_related('content_type')