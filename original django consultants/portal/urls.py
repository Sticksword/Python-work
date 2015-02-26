__author__ = 'Michael'
# from django.conf.urls.defaults import *
from portal.views import *
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = patterns('',

    # Main web portal entrance.
    (r'^$', portal_main_page),
    (r'^new_user/$', get_name),
    url('^register/', CreateView.as_view(
            template_name='registration/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    url('^accounts/', include('django.contrib.auth.urls')),

)

urlpatterns += staticfiles_urlpatterns()