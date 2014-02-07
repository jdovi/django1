from django.conf.urls import patterns, url

from notify import views

urlpatterns = patterns('',
    #ex /notify/
	url(r'^$', views.index, name='index'),
	#ex /notify/1
	url(r'^(?P<customer>\d+)/$', views.detail, name='detail'),
	#ex /notify/1/results/
	url(r'^(?P<customer>\d+)/results/$', views.results, name='results'),
	#ex /notify/1/vote/
	url(r'^(?P<customer>\d+)/vote/$', views.vote, name='vote'),
)
