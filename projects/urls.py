from django.conf.urls import patterns, url, include

from projects import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create_project/$', views.CreateProjectView.as_view(),
        name='create'),
    url(r'^add/$', views.AddProjectView.as_view(), name='add'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
)
