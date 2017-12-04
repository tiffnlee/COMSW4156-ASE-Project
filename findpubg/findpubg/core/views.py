from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from findpubg.core.forms import SignUpForm
from findpubg.core.forms import SearchForm
from findpubg.core.models import Search

def start(request):
    return render(request, 'start.html')

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
    template = loader.get_template('user_page.html')
    form = Search.objects.get(user_id=user_id)
    form = {
        'form' : form,
    }
    return HttpResponse(template.render(form, request))

def search_survey(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if (form.is_valid() and request.user.is_authenticated()):
            search_obj = form.save(False)
            search_obj.user_id = request.user
            if(Search.objects.filter(user_id=search_obj.user_id)):
                old_entries = Search.objects.filter(user_id = search_obj.user_id).delete()
            form.save()
            return redirect('user_board')
    else:
        form = SearchForm()
    return render(request, 'search.html', {'form': form})

def sort_search_by_date_joined(request):
    most_recent_joined = Search.objects.order_by('-date_joined')
    template = loader.get_template('user_board.html')
    context = {
        'lst' : most_recent_joined,
    }
    return HttpResponse(template.render(context, request))


def show_duos(request):
    duos = Search.objects.filter(team_choices__contains='DUOS')
    template=loader.get_template('user_board.html')
    context= {
 	      'lst' : duos,
    }
    return HttpResponse(template.render(context, request))


def show_squads(request):
    squads = Search.objects.filter(team_choices__contains='SQUADS')
    template=loader.get_template('user_board.html')
    context= {
   	        'lst': squads,
    }
    return HttpResponse(template.render(context, request))

def show_squadsfps(request):
    squadsfps = Search.objects.filter(team_choices__contains='SQUADS FPS')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':squadsfps,
    }
    return HttpResponse(template.render(context, request))

def show_duosfps(request):
    duosfps = Search.objects.filter(team_choices__contains='DUOS FPS')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':duosfps,
    }
    return HttpResponse(template.render(context, request))

def show_eu(request):
    eu = Search.objects.filter(region_choices__contains='EU')
    template=loader.get_template('user_board.html')
    context= {
	       'lst': eu,
    }
    return HttpResponse(template.render(context, request))

def show_as(request):
    asia = Search.objects.filter(region_choices__contains='AS')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':asia,
    }
    return HttpResponse(template.render(context, request))

def show_na(request):
    na = Search.objects.filter(region_choices__contains='NA')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':na,
    }
    return HttpResponse(template.render(context, request))

def show_oc(request):
    oc = Search.objects.filter(region_choices__contains='OC')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':oc,
    }
    return HttpResponse(template.render(context, request))

def show_sa(request):
    sa = Search.objects.filter(region_choices__contains='SA')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':sa,
    }
    return HttpResponse(template.render(context, request))


def show_sea(request):
    sea = Search.objects.filter(region_choices__contains='SEA')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':sea,
    }
    return HttpResponse(template.render(context, request))

def show_kr(request):
    kr = Search.objects.filter(region_choices__contains='KR')
    template=loader.get_template('user_board.html')
    context= {
	       'lst':kr,
    }
    return HttpResponse(template.render(context, request))

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
