from django.utils import timezone
from django.test import TestCase
from .models import Search

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
