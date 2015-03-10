from django.conf.urls import patterns, url
from GiggleBit import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^~/(?P<tilde_slug>[-\w]+)/$', views.tilde, name='tilde'),
        )
