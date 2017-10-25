from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from findpubg.core.forms import SignUpForm
from findpubg.core.forms import SearchForm
from findpubg.core.models import Search


@login_required
def home(request):
    return render(request, 'home.html')

def user_board(request):
	lst = Search.objects.all()
	template = loader.get_template('user_board.html')
	context = {
		'lst' : lst,
	}
	return HttpResponse(template.render(context, request))

def user_page(request, user_id):
	form= Search.objects.get(user_id = user_id)
	response = ("UserId: %s <br> "
                "SteamId: %s <br> "
                "Email: %s <br> "
                "Team Preferences: %s <br> "
                "Region: %s <br> ")
	return HttpResponse(response % (form.user_id, form.steam_id,form.email,
                                    form.team_choices, form.region_choices))

def search_survey(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_board')
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
