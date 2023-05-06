
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

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact me',
            'message':'',
            'year':datetime.now().year,
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
            'message':'Your application description page.',
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
    if request.method == "POST":
        user_form = UserForm(request.POST, instance = request.user)
        profile_form = ProfileForm(request.POST, instance = request.user.profile)
        if user_form.is_valid() & profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Account Updated'))
        else:
            messages.error(request, ('POST request failed, database not updated'))


    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance = request.user.profile)
    assert isinstance(request, HttpRequest)
    return render(
        request, 'app/learn.html', {"user": request.user, "user_form": user_form, "profile_form": profile_form})


def get_meta_string(request):
    meta_info = request.META.get('HTTP_USER_AGENT' , '')
    return meta_info