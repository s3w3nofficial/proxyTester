#!/usr/bin/env python
#-*- coding: utf-8 -*-

import urllib
import re
import checkCrawlerd as cc
import os
import sys

def check_if_proxy_works(ip, port):
	if not os.path.exists("crawlerd.txt"):
		    open('crawlerd.txt', 'w+')
	else:
		if cc.check_file_crawlerd(ip) == False:
					
			proxy = {'http' : 'http://' + ip + ':' + str(port)}
			try:
				proxy = urllib.urlopen("http://httpbin.org/ip", proxies=proxy).read()
				proxy = re.findall(r'"([^"]*)"', proxy)
	
				if ip in proxy[1]:
					cc.write_to_crawlerd(ip)
					cc.write_to_working(ip, port)
					return True
				else:
					cc.write_to_crawlerd(ip)
					cc.write_to_not_working(ip, port)
					return False
			except KeyboardInterrupt:
				print "Ctrl+C was pressed. Quitting. "
				sys.exit(0)
			except:
				return "error"
		else:
			if cc.check_file_crawlerd(ip) == False:
				cc.write_to_crawlerd(ip)
			return "already-cralwerd"
