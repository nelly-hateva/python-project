from django.conf.urls import patterns, url
from django.conf.urls.defaults import include

from projects import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
)
