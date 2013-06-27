from django.conf.urls import patterns, url, include

from projects import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^create_project/$', views.CreateProjectView.as_view(),
        name='create'),
    url(r'^add/$', views.AddProjectView.as_view(url='/projects'), name='add'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^create_issue/$', views.CreateIssueView.as_view(),
        name='create_issue'),
    url(r'^add_issue/$', views.AddIssueView.as_view(url='/projects'),
        name='add_issue'),
)
