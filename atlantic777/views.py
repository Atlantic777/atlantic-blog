from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.template import RequestContext

menu = {'menu' : ['Home', 'Blog', 'About', 'Contact', 'Wiki']}


class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()

def index(request):
	return render_to_response('home.html', menu)

def wiki(request):
	return redirect("https://atlantic777.lugons.org/wiki")

def login_page(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(username=username, password=password)

	if user is not None:
		if user.is_active:
			login(request, user)
			return HttpResponse("You did it")
		else:
			return HttpResponse("Dissabled acc")
	else:
		form = LoginForm()
		return render_to_response("login.html", {'form':form}, RequestContext(request))

def logout_page(request):
	logout(request)
	return HttpResponse("Probably logged out.")
