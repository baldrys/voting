from django.conf.urls import url

from voting import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^active-votes/$', views.active_votes_view, name='active-votes'),
    url(r'^completed-votes/$', views.completed_votes_view, name='completed-votes'),
    url(r'^vote/(?P<id>\d+)/$', views.detail_vote_view, name='detail-vote'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)