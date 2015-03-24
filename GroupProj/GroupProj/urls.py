from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from registration.backends.simple.views import RegistrationView

class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/gigglebit/add_profile/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'GroupProj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('GiggleBit.urls')),
    url(r'^gigglebit/', include('GiggleBit.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
)

handler404 = 'GiggleBit.views.bad_url'
handler500 = 'GiggleBit.views.bad_url'

if settings.DEBUG:
    urlpatterns += patterns(
                            'django.views.static',
                            (r'media/(?P<path>.*)',
                             'serve',
                             {'document_root': settings.MEDIA_ROOT}), )
