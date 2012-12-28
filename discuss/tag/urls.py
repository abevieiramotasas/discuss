from django.conf.urls import patterns, include, url
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('tag.views',
	url(r'^$', 'index'),
	url(r'^autoescape$', 'autoescape'),
	url(r'^cycle$', 'cycle'),
	url(r'^debug$', 'debug'),
)
