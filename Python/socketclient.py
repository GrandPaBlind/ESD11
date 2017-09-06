#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : Socket	Client							#
#DAte : 05/09/2017								#
#Author : GrandPa								#
################################################# 

 	
#################################################
#Import externals functions: 

import socket

#################################################
#Def local or global: 

hote = '192.168.23.129'
port = 4848

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)




#################################################
#Programm Body:

mysock.connect((hote, port))

mysock.send(u"Message")

mysock.close()
