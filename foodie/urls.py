from django.conf.urls import patterns, include, url
#import Restaurant.urls 
from Restaurant.views import *
from settings import *
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'foodie.views.home', name='home'),
    # url(r'^foodie/', include('foodie.foo.urls')),
    #(r'^', include('Restaurant.urls')),
    (r'^$',index),
	#(r'^search$',search_result),
	(r'^search/(?P<path>.*)/$', item_select),
	(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT}),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
