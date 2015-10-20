from django.conf.urls import patterns, include, url
from django.contrib import admin
from qttraining import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'qttraining.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login', views.login),
    #url(r'^admin/', include(admin.site.urls)),
)
