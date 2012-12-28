from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'discuss.views.home', name='home'),
    # url(r'^discuss/', include('discuss.foo.urls')),

    url(r'^tag/', include('tag.urls')),
    url(r'^', include('front.urls')),
)
