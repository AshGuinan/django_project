from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from datetime import datetime
from message_app.models import LoggedUser
from django.template import RequestContext
from django.shortcuts import render_to_response

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/profile/')

    else:
        form=UserCreationForm()

    return render(request,
                  "registration/register.html",
                  {'form':form})

def welcome(request):
    return render(request,'welcome.html')

def add_photo(request):
    return render(request,'add_photo.html')

def logged(request):
  logged_users = LoggedUser.objects.all().order_by('username')
  return render_to_response('users/logged.html',
                            {'logged_users': logged_users},
                            context_instance=RequestContext(request))


