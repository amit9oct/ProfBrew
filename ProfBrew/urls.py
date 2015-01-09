from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProfBrew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('Users.views',
    url(r'^home/$', 'home'),
    url(r'^login/$','login_page'),
    url(r'^profile/$', 'verify_credentials'),
    url(r'^register/$','register'),
    url(r'^register/student/$','register_student'),
    url(r'^username_present/$','username_present'),
    url(r'^update/$','update'),
)
