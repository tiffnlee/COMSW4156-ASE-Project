from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from findpubg.core.models import Search

TEAM_CHOICES = (
    ('DUOS', 'DUOS'),
    ('SQUADS', 'SQUADS'),
    ('DUOS FPS', 'DUOS FPS'),
    ('SQUADS FPS', 'SQUADS FPS')
)

REGION_CHOICES = (
    ('NA', 'North America'),
    ('EU', 'Europe'),
    ('AS', 'Asian'),
    ('OC', 'Oceania'),
    ('SA', 'South America'),
    ('SEA', 'South East Asia'),
    ('KR/JP', 'Korea/Japan')
)

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )

class SearchForm(forms.ModelForm):
    class Meta:
        model = Search
        fields = ('user_id', 'steam_id', 'team_choices', 'region_choices', 'email', )
