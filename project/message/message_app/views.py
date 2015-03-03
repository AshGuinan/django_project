from django.shortcuts import render
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect

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

