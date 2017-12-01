from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from machina.app import board

from findpubg.core import views as core_views

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', core_views.home, name='home'),
    url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', core_views.user_page, name='user_page'),
    url(r'^user_board/$', core_views.user_board, name='user_board'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^search/$', core_views.search_survey, name='search'),
    url(r'^start/$', core_views.start, name='start'),
    url(r'^user_board/sort_by_date_joined/$', core_views.sort_search_by_date_joined, name='sort_by_date_joined'),
	url(r'^user_board/sort_by_region_preference/$', core_views.sort_by_region_preference, name='sort_by_region_preference'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^user_board/sort_by_team_preference/$', core_views.sort_by_team_preference,name='sort_by_team_preference'),
    # Apps
    url(r'^forum/', include(board.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
