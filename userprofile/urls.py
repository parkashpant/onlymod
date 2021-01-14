from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns=[
    path('view_profile', views.view_profile, name='view_profile'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    # path('list_profiles', views.list_profiles, name='list_profiles')
]