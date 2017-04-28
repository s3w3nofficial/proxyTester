#!/usr/bin/env python
#-*- coding: utf-8 -*-
import crawler as c
import checkProxy as checker

def main():
	ip_port = c.get_ip_port()
	for ip in ip_port[0]:
		for port in ip_port[1]:
			print ip, port
			print checker.check_if_proxy_works(ip, port)
	
if __name__ == "__main__":
	main()
