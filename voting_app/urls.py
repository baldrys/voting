from django.conf.urls import url

from voting import settings
from . import views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^active-votes/$', views.activeVotes, name='active-votes'),
    url(r'^completed-votes/$', views.completedVotes, name='completed-votes'),

    url(r'^vote/(?P<id>\d+)/$', views.detailVote, name='detail-vote'),
    # url(r'complete-vote/(?P<slug>[\w-]+)/^$', views.home, name='home'),
]
if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)