import views
import templates.index 
from django.conf.urls.defaults import patterns, include, url
from django.views.static import * 
from django.conf import settings

urlpatterns = patterns('',
(r'^',index),
#(r'^search$',search_result),
(r'^search/(?P<path>.*)/$', item_select),
(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
#if settings.DEBUG:
    # Allow django.staticfiles to do its job itself
    # in debug mode.
 #   urlpatterns += patterns(
  #      '',
   #     (r'', include('staticfiles.urls')),
    #)
