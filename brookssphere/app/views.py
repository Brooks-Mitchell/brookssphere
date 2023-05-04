
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
     
     assert isinstance(request, HttpRequest)
     return render(
        request,
        'app/learn.html', {"user": request.user, "user_form": user_form, "profile_form": profile_form})