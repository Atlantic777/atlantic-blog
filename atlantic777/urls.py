from django.conf.urls import patterns, include, url
from views import index, wiki

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'atlantic777.views.home', name='home'),
    # url(r'^atlantic777/', include('atlantic777.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   url(r'^admin/', include(admin.site.urls)),
   url(r'^blog/', include('blog.urls')),
   url(r'^home/$', index),
   url(r'^wiki/$', wiki),
   url(r'^comments/', include('django.contrib.comments.urls')),
   url(r'^pages/', include('django.contrib.flatpages.urls')),
)

urlpatterns+= patterns('django.contrib.flatpages.views',
   url(r'^about/$^', 'flatpage', {'url': '/about/'}, name='about'),
)
