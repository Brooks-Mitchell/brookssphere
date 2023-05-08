

from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, UserForm, ProfileForm
from django.contrib import messages
from django.shortcuts import  render, redirect

#from urllib import request
from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'meta_info': get_meta_string(request)
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About Me',
        }
    )


def register_request(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/learn/")
        messages.error(request, "Invalid registration")
    form = NewUserForm()
    return render(request, 'app/register.html', {"form":form})

@login_required
def learn(request):

    changed_profile_data = None
    changed_user_data = None

    if request.method == "POST":
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() & profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Account Updated'))
        
            # TODO: move this into a function
            if user_form.has_changed():
                changed_user_data = user_form.changed_data
                increment_operations(request, changed_user_data)
        
            if profile_form.has_changed():
                changed_profile_data = profile_form.changed_data
                increment_operations(request, changed_profile_data)

        else:
            messages.error(request, ('POST request failed, database not updated'))
            post_data = user_form.errors
            


    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance = request.user.profile)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'app/learn.html', 
        {
            "user": request.user, 
            "user_form": user_form, 
            "profile_form": profile_form,
            "changed_user_data": changed_user_data,
            "changed_profile_data": changed_profile_data
        }
    )


def get_meta_string(request):
    meta_info = request.META.get('HTTP_USER_AGENT' , '') #REMOTE_ADDR = IP address
    return meta_info

def increment_operations(request, user_data = None, profile_data = None):
    try:
        request.user.profile.operations_performed += len(user_data)
        request.user.profile.operations_performed += len(profile_data)
    except:
        print("nonetype len error")
    request.user.profile.save()
 
