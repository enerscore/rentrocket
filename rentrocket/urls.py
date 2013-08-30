from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


#first argument to patterns tells the prefix for the module callback parameter
#here we use '' to keep things generic
urlpatterns = patterns('',
    # Examples:
    url(r'^building/', include('building.urls')),
    url(r'^$', 'rentrocket.views.home', name='home'),
    # url(r'^rentrocket/', include('rentrocket.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


#only serve static files in development
#in production, they should be served by production server
#https://docs.djangoproject.com/en/1.2/howto/static-files/
## if settings.DEBUG:
##     urlpatterns += patterns('',
##         (r'^js/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.LOCAL_ROOT + '/static/js'}),
##         (r'^css/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.LOCAL_ROOT + '/static/css'}),
##         (r'^images/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.LOCAL_ROOT + '/static/images'}),
##         (r'^favicon.png$', 'django.views.static.serve', {'document_root': settings.LOCAL_ROOT + '/static/images/', 'path': 'favicon.png'}),
##         (r'^apple-touch-icon.png$', 'django.views.static.serve', {'document_root': settings.LOCAL_ROOT + '/static/images/', 'path': 'apple-touch-icon.png'}),
##     )
