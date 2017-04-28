#!/usr/bin/env python
#-*- coding: utf-8 -*-

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
