
from urllib import request
from django.contrib.auth.forms import UserCreationForm
from .forms import NewUserForm, UserForm, ProfileForm
from django.contrib import messages
from django.shortcuts import  render, redirect


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
            'year':datetime.now().year,
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
            'year':datetime.now().year,
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
            return redirect("/")
        messages.error(request, "Invalid registration")
    form = NewUserForm()
    return render(request, 'app/register.html', {"form":form})

@login_required
def learn(request):
    post_data = None
    if request.method == "POST":
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() & profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Account Updated'))
        else:
            messages.error(request, ('POST request failed, database not updated'))
            post_data = user_form.errors

        if user_form.has_changed():
            post_data = user_form.changed_data
            increment_operations(request, post_data)
            


    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance = request.user.profile)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'app/learn.html', 
        {
            "user": request.user, 
            "user_form": user_form, 
            "profile_form": profile_form,
            "post_data": post_data
        }
    )


def get_meta_string(request):
    meta_info = request.META.get('HTTP_USER_AGENT' , '')
    return meta_info

def increment_operations(request, post_data):
    request.user.profile.operations_performed += len(post_data)
    request.user.profile.save()
    return post_data
