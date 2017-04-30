#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import crawler as c
import checkProxy as checker
import sys

def main():
	ip_port = c.get_ip_port()
	"""
	print ip_port
	for ip in ip_port[0]:
		for port in ip_port[1]:
			print ip, port
	"""

	i = 0
	while i < len(ip_port[0]):
		check = checker.check_if_proxy_works(ip_port[0][i], int(ip_port[1][i]))
		print ip_port[0][i], ip_port[1][i], check

		i += 1

	
if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt as e:
		print("Ctrl+C was pressed. Quitting.")
		sys.exit(0)
