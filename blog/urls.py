from django.conf.urls import patterns, include, url
from views import BlogView, PostView, ArchiveView
from atlantic777.views import menu

urlpatterns = patterns('', 
		url(r'^$', BlogView.as_view()),
		url(r'(?P<pk>\d+)', PostView.as_view()),
		url(r'archive', ArchiveView.as_view()),
		)
