from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/',
                           include(admin.site.urls)),

                       url(r'^$',
                           'index.views.home',
                           name='home'),

                       url(r'^unixtools/',
                           include('index.urls')),

)

handler404 = 'index.views.my_custom_404'