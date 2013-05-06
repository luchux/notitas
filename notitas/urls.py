from django.conf.urls import patterns, include, url
from django.contrib import admin
from notes.views import index, add, get_list_notes
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^notes/$', get_list_notes),
    url(r'^notes/add/', add),
    url(r'^admin/', include(admin.site.urls)),

)
