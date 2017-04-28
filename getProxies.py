#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re
import sys

def get_working_proxies():
	with open("working.txt") as f:
		lines = f.readlines()
	
	otp = []

	for line in lines:
		line = line.strip('\n')
		otp.append(line)
	
	return otp 

def get_not_working_proxies():
	with open("notworking.txt") as f:
		lines = f.readlines()
	
	otp = []

	for line in lines:
		line == line.strip('')
		otp.append(line)
	
	return otp

def check_proxy(ip, port):
	try:
		proxy = {'http' : 'http//' + ip + ':' + str(port)}
		proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
		proxy = re.findall(r'"([^"]*)"', proxy)
		if ip in proxy:
			return True
		else:
			return False
		except KeyboardInterrupt:
			print "Ctrl+c was pressed. Exiting!!!"
			sys.exit(0)
		except:
			return "connection lost"
