from django.conf.urls import patterns, include, url

from django.contrib import admin
import ctapp.urls
import matches.urls

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gw2ct.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^matches/', include(matches.urls)),
    url(r'^', include(ctapp.urls)),
)
