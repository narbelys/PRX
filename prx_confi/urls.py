# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', 'PRX.views.index'),
	url(r'^$', 'PRX.views.idioma'),
	url(r'^inicio/$', 'PRX.views.index'),
	url(r'^quienesSomos/$', 'PRX.views.quienesSomos'),
	url(r'^contacto/$', 'PRX.views.contacto'),
	
	url(r'^home/$', 'PRX.views.indexI'),
	url(r'^about/$', 'PRX.views.quienesSomosI'),
	url(r'^contact/$', 'PRX.views.contactoI'),
	
	url(r'^investors/$', 'PRX.views.inversionistas'),
	url(r'^license/$', 'PRX.views.license'),
	#url(r'^nuevo/$', 'PRX.views.inversionistas'),
	
    # Examples:
    # url(r'^$', 'prx_vademecum.views.home', name='home'),
    # url(r'^prx_vademecum/', include('prx_vademecum.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()