from django.utils import timezone
from django.test import TestCase
from .models import Search, Profile
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your tests here.
class SearchModelTest(TestCase):
	time = timezone.now
	def setUp(self):
		global time
		time = timezone.now
		userA = Search.objects.create(user_id='userA',steam_id='UA',team_choices='TeamA',region_choices='NA',email='userA@gmail.com')

		userB = Search.objects.create(user_id='userB',steam_id='UB',team_choices='TeamB',region_choices='NA',email='userB@gmail.com')

		userC = Search.objects.create(user_id='userC',steam_id='UC',team_choices='TeamC',region_choices='NA',email='userC@gmail.com')

		userD = Search.objects.create(user_id='userD',steam_id='UD',team_choices='TeamD',region_choices='NA',email='userD@gmail.com')

		userE = Search.objects.create(user_id='userE',steam_id='UE',team_choices='TeamE',region_choices='NA',email='userE@gmail.com')

		userD = Search.objects.create(user_id='userF',steam_id='UF',team_choices='TeamF',region_choices='NA',email='userF@gmail.com')

	def test_sort_team(self):
		ordered_team_preferences = Search.objects.order_by('team_choices')
		self.assertTrue(ordered_team_preferences[0].team_choices == 'TeamA')
	def test_sort_user_id(self):
		ordered_team_preferences = Search.objects.order_by('user_id')
		self.assertTrue(ordered_team_preferences[0].user_id == 'userA')
	def test_sort_steam_id(self):
		ordered_team_preferences = Search.objects.order_by('steam_id')
		self.assertTrue(ordered_team_preferences[0].steam_id == 'UA')
	def test_sort_region_choices(self):
		ordered_team_preferences = Search.objects.order_by('region_choices')
		self.assertTrue(ordered_team_preferences[0].region_choices == 'NA')

class RegistrationFormTests(TestCase):
    def test_registration_form(self):
		invalid_data_dicts = [
            # Non-alphanumeric username.
            {
            'data':
            { 'username': 'foo/bar',
              'birth_date': '1996-09-11',
              'password1': 'foo',
              'password2': 'foo' },
            'error':
            ('username', [u'Enter a valid username. This value may contain only English letters, numbers, and @/./+/-/_ characters.'])
            },
			{
            'data':
            { 'username': 'foo',
              'birth_date': 'best',
              'password1': 'foo',
              'password2': 'foo' },
            'error':
            ('birth_date', [u'Enter a valid date.'])
            },
			{
            'data':
            { 'username': 'foo',
              'birth_date': '0000-00-00',
              'password1': 'foo',
              'password2': 'foo' },
            'error':
            ('birth_date', [u'Enter a valid date.'])
            },
			{
            'data':
            { 'username': 'foo',
              'birth_date': '1996-09-11',
              'password1': 'fo',
              'password2': 'foo' },
            'error':
            ('password2', [u"The two password fields didn't match."])
            },
        ]

		for invalid_dict in invalid_data_dicts:
			form = forms.SignUpForm(data=invalid_dict['data'])
			self.failIf(form.is_valid())
			self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

		form = forms.SignUpForm( data={ 'username': 'foo',
										'birth_date': '1996-09-11',
										'password1': 'foo',
										'password2': 'foo' } )
		self.failUnless(form.is_valid())
