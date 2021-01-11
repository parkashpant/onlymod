from django.urls import path
from . import views

app_name = 'modprofile'

urlpatterns=[
    path('user_profile', views.user_profile, name='user_profile'),

]