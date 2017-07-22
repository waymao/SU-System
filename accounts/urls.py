from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reset$', views.reset, name='reset'),
    url(r'^activate$', views.activate, name='activate'),
    url(r'^login$', views.log_user_in, name='login'),
#    url(r'^login_success$', views.login_success, name='login_success'),
    url(r'^logout$', views.log_user_out, name='logout')
]