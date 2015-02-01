from django.conf.urls import patterns, include, url
from django.contrib import admin

INTERNAL = 1
EXTERNAL = 2
CALL_TYPE = {(INTERNAL,'Internal'),(EXTERNAL,'External'),}
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProfBrew.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('Users.views.home.home',
    url(r'^home/$', 'home'),
)
urlpatterns += patterns('Users.views.login.login',
    url(r'^login/$','login'),
)
urlpatterns += patterns('Users.views.caller',
    url(r'^register/student/$','caller'),
    url(r'^caller/$','caller'),
    url(r'^add/review/$','caller'),
    url(r'^like/review/$','caller'),
)
urlpatterns += patterns('Users.views.register.register',
    url(r'^register/$','register'),
)
urlpatterns += patterns('SearchEngine.views.search',
    url(r'^search/$', 'search'),
)
mnemonics = {
    '/home/':'HOME',
    '/login/':'LOGIN_PAGE',
    '/register/':'VERIFY_CRED',
    '/caller/':'REGISTER_PAGE',
}