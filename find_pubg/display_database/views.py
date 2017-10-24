# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import User
from django.template import loader
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.

@login_required
def home(request):
    return render(request, 'home.html')

def user_board(request):
	lst = User.objects.all()
	template = loader.get_template('display_database/user_board.html')
	context = {
		'lst' : lst,
	}
	return HttpResponse(template.render(context, request))

def user_page(request, user_id):
	user= User.objects.get(user_id = user_id)
	response = ("UserId: %s <br> SteamId: %s <br> Email: %s")
	return HttpResponse(response % (user.user_id, user.steam_id,user.email))

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})