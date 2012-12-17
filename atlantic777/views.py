from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect

menu = {'menu' : ['Home', 'Blog', 'About', 'Contact', 'Wiki']}

def index(request):
	return render_to_response('home.html', menu)

def wiki(request):
	return redirect("https://atlantic777.lugons.org/wiki")
