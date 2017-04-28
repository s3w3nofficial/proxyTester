#!/usr/bin/env python
#-*- coding: utf-8 -*-
import crawler as c
import checkProxy as checker
import sys
import signal

def handleCtrlC():
	print "Ctrl+C was pressed. Exiting. "
	sys.exit(0)

def main():
	ip_port = c.get_ip_port()
	for ip in ip_port[0]:
		for port in ip_port[1]:
			print ip, port, checker.check_if_proxy_works(ip, port)
	
if __name__ == "__main__":
	signal.signal(signal.SIGINT, handleCtrlC)
	main()
