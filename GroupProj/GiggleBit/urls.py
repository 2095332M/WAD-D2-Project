from django.conf.urls import patterns, url
from GiggleBit import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^tilde/(?P<tilde_slug>[-\w]+)/$', views.tilde, name='tilde'),
        url(r'^image/(?P<image_slug>[\w\-]+)/$', views.image, name='image'),
        url(r'^add_profile/$', views.register_profile, name = 'add_profile'),
        )
