from django.test import TestCase
from django.utils import timezone

from . import forms
from . import views
from .forms import SearchForm
from .models import Search


# Create your tests here.
class SearchModelTest(TestCase):
    time = timezone.now
    def setUp(self):
        global time
        time = timezone.now
        userA = Search.objects.create(user_id='userA',steam_id='UA',team_choices='SQUADS',region_choices='NA',email='userA@gmail.com', rank=2)

        userB = Search.objects.create(user_id='userB',steam_id='UB',team_choices='DUOS',region_choices='OC',email='userB@gmail.com', rank=5)

        userC = Search.objects.create(user_id='userC',steam_id='UC',team_choices='SQUADS FPS',region_choices='SA',email='userC@gmail.com', rank=1)

        userD = Search.objects.create(user_id='userD',steam_id='UD',team_choices='DUOS FPS',region_choices='AS',email='userD@gmail.com', rank=10)

        userE = Search.objects.create(user_id='userE',steam_id='UE',team_choices='SQUADS',region_choices='EU',email='userE@gmail.com', rank=100000)

        userF= Search.objects.create(user_id='userF',steam_id='UF',team_choices='DUOS',region_choices='SEA',email='userF@gmail.com', rank = 0)

    def test_sort_region_choices(self):

	qs = Search.objects.all()
	
	
       # s = forms.FilterUser({'steam_id':'', 'team_choices':'', 'region_choices':'OC', 'rank':''}, queryset=qs) 
	
	s = forms.FilterUser({'team_choices':'DUOS FPS'})

	print s.qs[0].user_id

	self.assertTrue(s.qs[0].user_id == "userD")	

#	self.assertQuerysetEqual(s.qs[0].user_id, ["userD"], ordered=True) 

		


    #def test_sort_user_id(self):
    #    ordered_team_preferences = Search.objects.order_by('user_id')
    #    self.assertTrue(ordered_team_preferences[0].user_id == 'userA')
   # def test_sort_steam_id(self):
    #    ordered_team_preferences = Search.objects.order_by('steam_id')
    #    self.assertTrue(ordered_team_preferences[0].steam_id == 'UA')
    #def test_sort_region_choices(self):
     #   ordered_team_preferences = Search.objects.order_by('region_choices')
     #   self.assertTrue(ordered_team_preferences[0].region_choices == 'NA')

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
            #self.assertEqual(form.errors[invalid_dict['error'][0]], invalid_dict['error'][1])

            form = forms.SignUpForm(data={'username': 'foo',
                                       'birth_date': '1996-09-11',
                                       'password1': 'foo',
                                       'password2': 'foo' })
        self.failUnless(form.is_valid())

class SearchFormTest(TestCase):
    def test_SearchForm_valid(self):
        form1 = SearchForm(data={'user_id': "sampleuser", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "test@test.com"})
        self.assertTrue(form1.is_valid())

    def test_SearchForm_userid_invalid(self):
        form1 = SearchForm(data={'user_id': "sample>>user", 'steam_id': "sampleid", 'team_choices': "DUOS", 'region_choices': "NA", 'email': "test@test.com"})
        self.assertFalse(form1.is_valid())

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

