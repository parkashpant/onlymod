from django.shortcuts import render, redirect
from userprofile.models import UserProfileInfo
from .forms import UserProfileInfoForm, UserChangeForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def view_profile(request):
    return render(request, 'view_profile.html')


def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('view_profile')
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'edit_profile.html', {'form': form})


# def list_profiles(request):
#     lists = UserProfileInfo.objects.filter(user=request.user)
#     return render(request, {'lists': lists})
    