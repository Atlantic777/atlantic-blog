from django.conf.urls import patterns, include, url
from views import index, wiki, login_page, logout_page
from blog.api import PostResource, UserResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api =  Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(PostResource())

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
   url(r'^login/', login_page),
   url(r'^logout/', logout_page),
   url(r'^api/', include(v1_api.urls)),
   url(r'^$', index),
)

urlpatterns+= patterns('django.contrib.flatpages.views',
   url(r'^about/$^', 'flatpage', {'url': '/about/'}, name='about'),
)
