#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from lxml import html
import requests

def get_ip_port():

	
	#page = requests.get('https://free-proxy-list.net/')
	headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/57.0.2987.98 Chrome/57.0.2987.98 Safari/537.36"}
	page = requests.get('https://hidemy.name/en/proxy-list/', headers=headers)
	#page = requests.get('https://hidemy.name/en/proxy-list/')
	page = html.fromstring(page.content)
	
	#https://hidemy.name/en/proxy-list/
	ips = page.xpath('//table/tbody/tr/td[position()=1]/text()')	
	ports = page.xpath('//table/tbody/tr/td[position()=2]/text()')
 	
	ip_list = []
	port_list = []

	for ip in ips:
		ip_list.append(ip)
	for port in ports:
		port_list.append(port)
	
	#print ip_list
	#print port_list	
	return ip_list, port_list
