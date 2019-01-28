from django.conf.urls import patterns, url


urlpatterns = patterns('default_group.views',
    url(r'^$', 'configure'),
)
