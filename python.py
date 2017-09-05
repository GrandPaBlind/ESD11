#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : Pendu									#
#DAte : 04/09/2017								#
#Author : Napol Stevy							#
################################################# 


#################################################
#Import externals functions: 

#from tkinter Import *


#################################################
#Define local or global: 

keyword = "hello"
#keyword = ["h","e","l","l","o"]

rep = len(keyword)

fchoice = "False choice, try again"

tchoice = "You find right letter, well done"

#################################################
#Programm Body:
i = 0
r = 0
while r < rep:

	ri = raw_input('Choose a letter!')
	if any(ri in k for k in keyword):
		print "%s" %(tchoice)
		i = i + 1
		if ri == 'h':
			print keyword[0]
		elif ri == 'e':
			print keyword[1]
			
		if i == rep :
			print "WIN"
			break 

	else:
		print "%s" %(fchoice)
		r = r + 1
		
			

				
	

			
			

	