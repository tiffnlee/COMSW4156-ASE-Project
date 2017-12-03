from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from machina.app import board

from findpubg.core import views as core_views
from django.views.generic import RedirectView
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', core_views.start, name='start'),
    url(r'^(?P<user_id>[a-zA-Z0-9_]+)/user_page/$', core_views.user_page, name='user_page'),
    url(r'^user_board/$', core_views.user_board, name='user_board'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^search/$', core_views.search_survey, name='search'),
    url(r'^home/$', core_views.home, name='home'),
	url(r'^user_board/sort_by_date_joined/$', core_views.sort_search_by_date_joined, name='sort_by_date_joined'),
	url(r'^admin/', include(admin.site.urls)),
    url(r'^user_board/show_duos/$', core_views.show_duos, name='show_duos'),
    url(r'^user_board/show_squads/$', core_views.show_squads, name='show_squads'),
    url(r'^user_board/show_duosfps/$', core_views.show_duosfps, name='show_duosfps'),
    url(r'^user_board/show_squadsfps/$', core_views.show_squadsfps, name='show_squadsfps'),
    url(r'^user_board/show_eu/$', core_views.show_eu, name='show_eu'),
    url(r'^user_board/show_as/$', core_views.show_as, name='show_as'),
    url(r'^user_board/show_na/$', core_views.show_na, name='show_na'),
    url(r'^user_board/show_oc/$', core_views.show_oc, name='show_oc'),
    url(r'^user_board/show_sa/$', core_views.show_sa, name='show_sa'),
    url(r'^user_board/show_sea/$', core_views.show_sea, name='show_sea'),
    url(r'^user_board/show_kr/$', core_views.show_kr, name='show_kr'),
    # Apps
    url(r'^forum/', include(board.urls)),
    url(r'^forum/$', RedirectView.as_view(url='http://127.0.0.1:8000/forum/'), name='forum'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
