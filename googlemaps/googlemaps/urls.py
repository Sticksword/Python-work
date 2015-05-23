from django.conf.urls import patterns, include, url
from django.contrib import admin

# Import custom modules
import settings


admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'googlemaps.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('waypoints.urls')),
)
