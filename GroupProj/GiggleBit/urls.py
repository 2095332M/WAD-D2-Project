from django.conf.urls import patterns, url
from GiggleBit import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^(?P<page>\d+)/$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^tilde/(?P<tilde_slug>[-\w]+)/$', views.tilde, name='tilde'),
        url(r'^tilde/(?P<tilde_slug>[-\w]+)/(?P<page>\d+)/$', views.tilde, name='tilde'),
        url(r'^image/(?P<image_slug>[\w\-]+)/$', views.image, name='image'),
        url(r'^add_profile/$', views.register_profile, name = 'add_profile'),
        url(r'^addimage/$', views.add_image, name='add_image'),
        url(r'^submit_comment/$', views.submit_comment, name='submit_comment'),
        url(r'^like_category/$', views.like_category, name='like_category'),
        url(r'^suggest_category/$', views.suggest_category, name='suggest_category'),
        )
