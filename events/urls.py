from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^past_events/$', views.history, name='history'),
    url(r'^(?P<event_hash>[a-zA-Z0-9_.+]+)/$', views.detailed, name='detail'),
    url(r'^(?P<event_hash>[a-zA-Z0-9_.+]+)/edit/$', views.edit, name='edit'),
    url(r'^new$', views.add_new, name='add')
]
