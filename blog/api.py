from tastypie.resources import ModelResource, ALL
from blog.models import Post
from tastypie.authorization import  Authorization
from tastypie.authentication import  BasicAuthentication, Authentication
from django.contrib.auth.models import User
from tastypie import fields

class UserResource(ModelResource):
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		excludes = ['is_staff', 'is_active', 'email', 'is_superuser', 'password']
		filtering = {'username':ALL,}
		authentication = Authentication()
		authorization = Authorization()

class PostResource(ModelResource):
	class Meta:
		queryset = Post.objects.all()
		resource_name = 'post'
		authentication = BasicAuthentication()
		authorization = Authorization()
