from django.shortcuts import render, redirect
from accounts.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# Home Page
def index(request):
    return render(request,'index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

# Logout
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# Registration 
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        # User validation
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            # Auto login after registration
            login(request, user, backend='django.contrib.auth.backends.ModelBackend') 
            return redirect('index')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',
                          {'user_form':user_form,
                           'registered':registered})

# Log-in                          
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Calling authentication
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.warning(request, 'Your account is inactive')
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            messages.error(request, 'You have entered the wrong credential')
            return HttpResponseRedirect('user_login')
    else:
        return render(request, 'login.html', {})

