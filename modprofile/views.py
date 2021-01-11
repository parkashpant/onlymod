from django.shortcuts import render, redirect
from .forms import UserProfileInfoForm

# Create your views here.

def user_profile(request):
    prof_update = False
    if request.method == 'POST':
        profile_form = UserProfileInfoForm(request.POST)
        if profile_form.is_valid:
            profile = profile_form.save(commit=False)
            profile.user = request.user
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                profile.save()
                prof_update = True
                return render(request, 'profile.html', {'prof_update':prof_update,'profile_data':profile_form.cleaned_data})
        else:
            print(profile_form.errors)
    else:
        profile_form = UserProfileInfoForm()
    return render(request,'profile.html',
                          {'profile_form':profile_form,
                           'prof_update':prof_update})



    