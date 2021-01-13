from django.shortcuts import render, redirect
from modprofile.models import UserProfileInfo
from .forms import UserProfileInfoForm
# from django.urls import reverse

# Create your views here.

def view_profile(request):
    return render(request, 'profile.html')

def update_profile(request):
    profile_update = False
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(request.POST, request.FILES)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            profile_update = True
            return render(request, 'profile.html', {'profile_update':profile_update})
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileInfoForm()
    return render(request,'profileu[].html',
                          {'profile_form':profile_form,
                           'profile_update':profile_update})


def users_profile_list(request):
    lists = UserProfileInfo.objects.filter(user=request.user)
    return render(request, {'lists': lists})
    