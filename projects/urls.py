from django.conf.urls import patterns, url, include

from projects import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create_project/$', views.CreateProjectView.as_view(), name='create'),
    url(r'^add/$', views.AddProjectView.as_view(url='/projects'), name='add'),
    url(r'^create_issue/(?P<pk>\d+)/$', views.CreateIssueView.as_view(), name='create_issue'),
    url(r'^add_issue/(?P<pk>\d+)/$', views.AddIssueView.as_view(url='/projects'), name='add_issue'),
    url(r'^issue/(?P<pk>\d+)/$', views.DetailIssueView.as_view(), name='issue'),
    url(r'^start/(?P<pk>\d+)/$', views.StartIssueView.as_view(), name='start'),
)
