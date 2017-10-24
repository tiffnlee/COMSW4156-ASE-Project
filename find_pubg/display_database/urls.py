from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', views.user_page, name='user_page'),
    url(r'^user_board/$', views.user_board, name='user_board'),
    url(r'^signup', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
]
