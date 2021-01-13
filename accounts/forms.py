from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']

    def clean_name(self):
        name = self.cleaned_data['first_name']
        name_l = name.lower()
        if name_l == "admin" or name_l == "onlyqual":
            raise ValidationError("User name can't be 'admin/onlyqual'")
        return name_l

    def clean_email(self):
        return self.cleaned_data['email'].lower()
