#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import os

def check_file_crawlerd(string): 
	with open("crawlerd.txt") as f:
	    lines = f.readlines()
	 
	for line in lines:
		line = line.strip('\n')
		if string == line:
			#print "file contain ip"
			return True
			break
	return False

def write_to_crawlerd(ip):
	d = "crawlerd.txt"
	if not os.path.exists(d):
		    open(d, 'w+')
	else:
		with open(d, "a") as f:
		    	f.write(ip+"\n") 

def write_to_working(ip, port):
	d = "working.txt"
	if not os.path.exists(d):
		    open(d, 'w+')
	else:
		with open(d, "a") as f:
			f.write(ip + " " + str(port) + "\n")

def write_to_not_working(ip, port):
	d = "notworking.txt"
	if not os.path.exists(d):
		    open(d, 'w+')
	else:
		with open(d, "a") as f:
			f.write(ip + " " + str(port) + "\n")

#print check_file_crawlerd("68.128.212.240")
