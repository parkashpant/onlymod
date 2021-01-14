from django.shortcuts import render, redirect
from accounts.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.

# Home Page
def index(request):
    return render(request,'index.html')

# Logout
@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

# Registration 
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():                                                                    # User validation
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')               # Auto-login after registration        
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
        user = authenticate(username=username, password=password)                                   # Calling authentication
        if user:
            if user.is_active:
                login(request,user)
                return redirect('index')
            else:
                messages.warning(request, 'Your account is inactive')
        else:
            messages.error(request, 'You have entered the wrong credential')
            return HttpResponseRedirect('login')
    else:
        return render(request, 'login.html', {})

