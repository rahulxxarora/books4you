from django.conf.urls import patterns, url
from one import views

urlpatterns = patterns('',
        url(r'^search_form/$', views.search_form),
        url(r'^search_form/search/$', views.search))
