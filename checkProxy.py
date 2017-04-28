#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re

def check_if_proxy_works(ip, port):
	proxy = {'http' : 'http://' + ip + ':' + str(port)}
	try:
		proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
		proxy = re.findall(r'"([^"]*)"', proxy)
	
		if ip in proxy[1]:
			return True
		else:
			return False
	except:
		return "error"
