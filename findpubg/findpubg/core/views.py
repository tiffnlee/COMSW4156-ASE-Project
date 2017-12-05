from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from findpubg.core.forms import SignUpForm
from findpubg.core.forms import SearchForm
from findpubg.core.forms import FilterUser
from findpubg.core.models import Search


def start(request):
    return render(request, 'start.html')

@login_required
def home(request):
    try:
        info = Search.objects.get(user_id = request.user)
        context = {
            'info' : info
        }
        return render(request, 'home.html', {'info': info})
    except Search.DoesNotExist:
        return render(request, 'home.html')

def user_board(request):
    lst = Search.objects.all()
    user_filter = FilterUser(request.GET, queryset=lst)
    return render(request, 'user_board.html', {'filter': user_filter})

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
