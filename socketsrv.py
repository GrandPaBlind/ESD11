#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : Socket	Serv							#
#DAte : 05/09/2017								#
#Author : GrandPa								#
################################################# 

#################################################
#Import externals functions: 

import socket

#################################################
#Def local or global: 

hote = ''
port = 5000

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.bind((hote, port))



#################################################
#Programm Body:

while 1:
        mysock.listen(5)
        conn, address = mysock.accept()
        print "{} connected".format( address )

        response = conn.recv(2048)
        if response != "":
                print response


conn.close()
mysock.close()
