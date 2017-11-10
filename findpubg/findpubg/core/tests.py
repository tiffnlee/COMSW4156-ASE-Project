from django.utils import timezone
from django.test import TestCase
from .models import Search
from .forms import SearchForm

# Create your tests here.
class SearchModelTest(TestCase):
	time = timezone.now
	def test_set_and_search(self):
		global time
		time = timezone.now
		userA = Search.objects.create(user_id='userA',steam_id='UA',team_choices='TeamA',region_choices='NA',email='userA@gmail.com')

		userB = Search.objects.create(user_id='userB',steam_id='UB',team_choices='TeamB',region_choices='NA',email='userB@gmail.com')

		userC = Search.objects.create(user_id='userC',steam_id='UC',team_choices='TeamC',region_choices='NA',email='userC@gmail.com')

		userD = Search.objects.create(user_id='userD',steam_id='UD',team_choices='TeamD',region_choices='NA',email='userD@gmail.com')

		userE = Search.objects.create(user_id='userE',steam_id='UE',team_choices='TeamE',region_choices='NA',email='userE@gmail.com')
		userD = Search.objects.create(user_id='userF',steam_id='UF',team_choices='TeamF',region_choices='NA',email='userF@gmail.com')
		
		ordered_team_preferences = Search.objects.order_by('team_choices')
		self.assertTrue(ordered_team_preferences[0].team_choices == 'TeamA')

class SearchFormTest(TestCase):
	def test_SearchForm_valid(self):
		form1 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "test@test.com"})
		self.assertTrue(form1.is_valid())

	def test_SearchForm_userid_invalid(self):
		form1 = SearchForm(data={'user_id': "sample>>user", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "test@test.com"})
		self.assertTrue(form1.is_valid())

	def test_SearchForm_choices_invalid(self):
		form1 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "LOL", 'region_choices': "NA", 'email': "test@test.com"})
		form2 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "LOL",'email': "test@test.com"})
		self.assertFalse(form1.is_valid())
		self.assertFalse(form2.is_valid())

	def test_SearchForm_email_invalid(self):
		form1 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "bademail"})
		form2 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "bademail@bad"})
		self.assertFalse(form1.is_valid())
		self.assertFalse(form2.is_valid())