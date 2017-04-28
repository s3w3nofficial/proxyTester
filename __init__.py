#!/usr/bin/env python
#-*- coding: utf-8 -*-
import crawler as c
import checkProxy as checker
import sys

def main():
	ip_port = c.get_ip_port()
	for ip in ip_port[0]:
		for port in ip_port[1]:
			print ip, port
			check = checker.check_if_proxy_works(ip, int(port)) 
			if check == "error" or check == False:
				print "next"
			else:
				print check
	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print "Ctrl+C was pressed. Quitting."
		sys.exit(0)
