#!/usr/bin/env python

#make the hash.py file that goes through all of the files on the system and then
#hash them. some do not need to be hashed however....

import os
import hashlib
#dont hash /dev, /proc, /run, /sys, tmp, /var/lib, /var/run/

def walkthrough():
	list = []
	badlist = ['/dev', '/proc', '/run', '/sys', 'tmp', '/var/lib', '/var/run/']
	for dirpath, dirs, files in os.walk('.'):
		if dirpath in badlist:
			pass
		else:
			print(dirpath) #this is part 1 and 2 completed now
#http://www.pythoncentral.io/hashing-strings-with-python/
def hashing(strr):
	byted = bytes(strr,'utf-8')
	h = hashlib.sha256(byted)
	print(h.hexdigest())
	


walkthrough()
	
