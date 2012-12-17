# Create your views here.
from django.views.generic import ListView, DetailView
from blog.models import Post
from atlantic777.views import menu
from django.http import HttpResponseRedirect

class BlogView(ListView):
	template_name="blog.html"
	queryset=Post.objects.all().order_by("-created")[:2]

	def get_context_data(self, **kwargs):
		context = super(BlogView, self).get_context_data(**kwargs)
		context['menu'] = menu['menu']
		return context

class PostView(DetailView):
	model = Post
	template_name="post.html"

	def get_context_data(self, **kwargs):
		context = super(PostView, self).get_context_data(**kwargs)
		context['menu'] = menu['menu']
		return context
class ArchiveView(ListView):
	template_name="archive.html"
	queryset=Post.objects.all().order_by("-created")

	def get_context_data(self, **kwargs):
		context = super(ArchiveView, self).get_context_data(**kwargs)
		context['menu'] = menu['menu']
		return context

