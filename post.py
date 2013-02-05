#!/usr/bin/python
import requests
import json
from getpass import getpass
from datetime import datetime

url = "http://localhost:8000/api/v1/post/"

username = ""
password = ""
title    = ""
text     = ""
date     = str(datetime.now())
head     = {"Content-Type":"application/json",}

while username == "":
	username = raw_input("Username: ")
	if username == "": print "Please enter a username!"

while password == "":
	password = getpass()
	if password == "": print "Please enter a password!"

while title == "":
	title = raw_input("Title: ")
	if title == "": print "Please enter a title!"

print "Text:"
while True:
	line = raw_input()
	if line == "\end": break
	else: text += line

creds     = (username, password)
post_data = json.dumps({"title":title, "text":text, "created":date})

resp = requests.post(url, headers=head, auth=creds, data=post_data)
print resp.status_code
