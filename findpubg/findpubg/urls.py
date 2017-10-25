from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from findpubg.core import views as core_views


urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', core_views.user_page, name='user_page'),
    url(r'^user_board/$', core_views.user_board, name='user_board'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^search/$', core_views.search_survey, name='search'),
]