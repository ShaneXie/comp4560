from django.conf.urls import patterns, include, url
from django.contrib import admin
from view_historical import views as vh_views

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', vh_views.index),
    url(r'^ajax/(\w+)/$', vh_views.loadAjaxData),
)
