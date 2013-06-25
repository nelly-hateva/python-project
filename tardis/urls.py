from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^projects/', include('projects.urls', namespace="projects")),
    url(r'^admin/', include(admin.site.urls)),
)
