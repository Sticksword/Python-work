__author__ = 'Michael'

from blog.views import *
from django.conf.urls import patterns, url


urlpatterns = patterns('',

    (r'^$', index),
    url(
    r'^blog/view/(?P<slug>[^\.]+).html',
    'blog.views.view_post',
    name='view_blog_post'),
    url(
    r'^blog/category/(?P<slug>[^\.]+).html',
    'blog.views.view_category',
    name='view_blog_category'),
    (r'^create_post/', create_post),
    (r'^search_form/', search_form)


)