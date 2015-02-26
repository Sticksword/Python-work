from django.conf.urls import patterns, include, url
from django.contrib import admin
from django_consultants.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
# from django.conf.urls.defaults import *


urlpatterns = patterns('',
    (r'^$', main_page),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    # Web portal.
    (r'^portal/', include('portal.urls')),

    # Serve static content.
    # (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    #     {'document_root': 'static'}),

    url(r'^admin/', include(admin.site.urls)),

    # Blog
    (r'^blog/', include('blog.urls')),
)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
