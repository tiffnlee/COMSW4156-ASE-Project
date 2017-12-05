from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from findpubg.core.models import Search
from findpubg.core.models import TEAM_CHOICES, REGION_CHOICES
import django_filters
from django_filters import filters


class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2')

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('steam_id', 'team_choices', 'region_choices', 'email', 'rank')

class FilterUser(django_filters.FilterSet):
    class Meta:
        model = Search
        fields = ('steam_id', 'team_choices', 'region_choices',)
