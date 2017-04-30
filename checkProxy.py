#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib
import re
import checkCrawled as cc
import os
import sys

def check_if_proxy_works(ip, port):
	if not os.path.exists("crawlerd.txt"):
		    open('crawlerd.txt', 'w+')

	if cc.check_file_crawlerd(ip) == False:			
		try:	
			proxy = {'http' : 'http://' + ip + ':' + str(port)}	
			proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
			proxy = re.findall(r'"([^"]*)"', proxy)
			if ip in proxy:
				cc.write_to_crawlerd(ip)
				cc.write_to_working(ip, port)
				return True
			else:
				cc.write_to_crawlerd(ip)
				cc.write_to_not_working(ip, port)
				return False
			
		except KeyboardInterrupt as e:
			print("Ctrl+C was pressed. Quitting. ")
			sys.exit(0)
		except:
			return "error"
	else:
		return "already crawled"

	return "error"
