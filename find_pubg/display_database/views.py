# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from models import User
from django.template import loader

# Create your views here.

def display_users(request):
	return HttpResponse("Welcome to the user board")

def board_info(request):
	lst = User.objects.all()
	template = loader.get_template('display_database/board_info.html')
	context = {
		'lst' : lst,
	}
	return HttpResponse(template.render(context, request))

def user_page(request, user_id):
	user= User.objects.get(user_id = user_id)
	response = ("UserId: %s <br> SteamId: %s <br> Email: %s")
	return HttpResponse(response % (user.user_id, user.steam_id,user.email))
