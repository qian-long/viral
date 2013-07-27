from django.conf.urls import patterns, url
import tweetmap.views as views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')

)
