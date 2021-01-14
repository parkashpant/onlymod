from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class UserForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['first_name','last_name','username','password','email']

