#!/usr/bin/python2
import urllib2, urllib, cookielib
from BeautifulSoup import BeautifulSoup
from datetime import datetime
from getpass import getpass
from sys import exit


LOGIN_URL = "http://localhost:8000/login/"

class Poster():
	def __init__(self):
		self.cj = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		self.login_form = BeautifulSoup(self.opener.open(LOGIN_URL).read())
		self.csrf = self.login_form.find('input', attrs={'name':'csrfmiddlewaretoken'}).attrMap
		self.set_creds()
		req = urllib2.Request(LOGIN_URL, urllib.urlencode(self.creds))
		self.opener.open(req).read()


	def set_creds(self):
		username = ''
		password = ''
		while username == '':
			username = raw_input("Username: ")

		while password == '':
			password = getpass()

		self.creds = {'username':username,
			      'password':password,
			      'remember': '',
			      'csrfmiddlewaretoken':self.csrf['value'] }

	def get_csrf(self):
		return self.creds.get('csrfmiddlewaretoken')

	def new_post(self):
		title = None
		while title is None:
			title = raw_input("Title: ")

		print "Text:"
		text = ''
		while True:
			line = raw_input()
			if line == "\end": break
			text += line + '\n'

		data = { 'title':title,
			 'text' : text,
			 'csrfmiddlewaretoken': self.get_csrf(),
			 'date':datetime.now(),
			}
		req = urllib2.Request("http://localhost:8000/blog/new/", urllib.urlencode(data))
		raw_html = self.opener.open(req).read()

client = Poster()
client.new_post()
