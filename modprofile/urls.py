from django.urls import path
from . import views

app_name = 'modprofile'

urlpatterns=[
    path('view_profile', views.view_profile, name='view_profile'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('users_profile_list', views.users_profile_list, name='users_profile_list')
]