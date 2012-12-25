from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('front.views',
    # Examples:
    # url(r'^$', 'discuss.views.home', name='home'),
    # url(r'^discuss/', include('discuss.foo.urls')),
    url(r'^$', 'main', name='main'),
    url(r'^server_side$', 'server_side', name='server_side'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'(.+\.html)$', 'direct_to_template'),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
