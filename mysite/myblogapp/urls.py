__author__ = 'Michael'

from django.conf.urls import patterns, url
from myblogapp.views import my_view

urlpatterns = patterns('',
    url(r'^$', my_view),
    # url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    # url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)