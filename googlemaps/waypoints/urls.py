__author__ = 'Michael'

from django.conf.urls import patterns, include, url


urlpatterns = patterns('waypoints.views',
    url(r'^$', 'index', name='waypoints-index'),
    url(r'^save$', 'save', name='waypoints-save'),
    url(r'^search$', 'search', name='waypoints-search'),
    url(r'^upload$', 'upload', name='waypoints-upload'),
)

