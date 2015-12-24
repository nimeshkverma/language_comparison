from django.conf.urls import patterns, url

from pyserver import views

urlpatterns = patterns('',
    url(r'^time_block$', views.time_block, name='time_block'),
    url(r'^crud$', views.crud, name='crud')
)