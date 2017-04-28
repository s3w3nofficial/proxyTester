#!/usr/bin/env python
#-*- coding: utf-8 -*-

def check_file_crawlerd(ip): 
	with open("crawlerd.txt") as f:
	    lines = f.readlines()
	 
	for line in lines:
		line = line.strip('\n')
		if ip == line:
			print "file contain ip"
			return True
			break
	return False

def write_to_crawlerd(ip):
	with open("crawlerd.txt", "a") as f:
	    f.write(ip) 

def write_to_working(ip, port):
	with open("working.txt", "a") as f:
		f.write(ip, port)

def write_to_not_working(ip, port):
	with open("notworking.txt", "a") as f:
		f.write(ip, port)
