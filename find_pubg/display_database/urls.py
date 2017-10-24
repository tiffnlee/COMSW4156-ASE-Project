from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.display_users, name='display_users'),
	url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', views.user_page, name='user_page'),
	url(r'^board_info/$', views.board_info, name='board_info'),
]


