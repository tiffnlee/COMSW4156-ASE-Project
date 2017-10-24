from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', views.user_page, name='user_page'),
	url(r'^user_board/$', views.user_board, name='user_board'),
]


