from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<event_hash>[a-f0-9]+)/$', views.detailed, name='detail'),
    url(r'^(?P<event_hash>[a-f0-9]+)/edit/$', views.edit, name='edit')
]
