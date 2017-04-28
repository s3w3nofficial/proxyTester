#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lxml import html
import requests

def get_ip_port():

	"""	
	#page = requests.get('https://free-proxy-list.net/')
	page = requests.get('https://hidemy.name/en/proxy-list/')
	page = html.fromstring(page.content)
	
	#https://hidemy.name/en/proxy-list/
	ips = page.xpath('//table/tbody/tr/td[position()=1]/text()')	
	ports = page.xpath('//table/tbody/tr/td[position()=2]/text()')
 	"""
	ip_list = ['107.0.69.165', '192.241.129.174', '108.14.231.223']
	port_list = ['3128', '3128', '3128']
	"""
	for ip in ips:
		ip_list.append(ip)
	for port in ports:
		port_list.append(port)
	"""
	#print ip_list
	#print port_list	
	return ip_list, port_list
