#!/usr/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import commands
import getpass
#import curses

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

class Server():
	fssh =""
	def Slogin(self):
		sshIP = raw_input ("Remote IP: ")
		sshUser = raw_input ("Input username: ")
		sshPass = getpass.getpass ("Input password: ")
		global fssh 
		fssh = "sshpass -p " + sshPass + " ssh -o StrictHostKeyChecking=no " + sshUser + "@" + sshIP
		optionsMenu()
		menu_choice()

	def blah():
		fsshSatus = commands.getstatusoutput(fssh)

		if fsshSatus[0] == 0:
			print (fsshSatus[1])
		elif fsshSatus[0] == 1280:
			print ("Incorrect login credentials.")
			print (fsshSatus[1])
		else:
			print (fsshSatus[1])

	def configServer():
		 
		#print (fssh)
		datecmd = fssh + " date"
		date = commands.getstatusoutput(datecmd)

		if date[0] == 0:
			print (date[1])
		elif date[0] == 1280:
			print ("Incorrect login credentials.")
			print (date[1])
		else:
			print (date[1])

	def httpdRestart(self):
		RHTTPD = fssh + " 'systemctl restart httpd'"
		restartHTTPD = commands.getstatusoutput(RHTTPD)
		if restartHTTPD[0] == 0:
			print ("Apache httpd restart successful.")
		else:
			print ("Error restarting server.")
			print (restartHTTPD[1])

def cont():
	raw_input ("Press enter to continue...")
	mainMenu()
	menu_choice()

def mainMenu():
		print (color.YELLOW + "\t\t\t\t\t-  -" + color.END )
		os.system("tput setaf 4")
		print ("""
\t .d8888b. 888                     888    .d8888b.                  .d888d8b         
\td88P  Y88b888                     888   d88P  Y88b                d88P" Y8P         
\t888    888888                     888   888    888                888               
\t888       888 .d88b. 888  888 .d88888   888        .d88b. 88888b. 888888888 .d88b.  
\t888       888d88""88b888  888d88" 888   888       d88""88b888 "88b888   888d88P"88b 
\t888    888888888  888888  888888  888   888    888888  888888  888888   888888  888 
\tY88b  d88P888Y88..88PY88b 888Y88b 888   Y88b  d88PY88..88P888  888888   888Y88b 888 
\t "Y8888P" 888 "Y88P"  "Y88888 "Y88888    "Y8888P"  "Y88P" 888  888888   888 "Y88888 
\t                                                                                888 
\t                                                                           Y8b d88P 
\t                                                                            "Y88P"  
                                                                      
		""")
		os.system("tput setaf 7")
		ws = " "
		print (4*ws,"-----------------------------------------------------------------------------------------------")
		print("\n\n")
		print ("""
		Log-in to remote server required:


		""")
		raw_input ("""
Enter to continue...
		""")
		


def optionsMenu():
	print ("""
		Press 1: To restart server
		Press 2: To create file
		Press 3: To create user
		Press 4: To mount a drive
		Press 0: To exit
		""")


def menu_choice():	
	server = Server()
	choice = int(raw_input("Enter your choice: "))
	if int(choice) == 1:
		server.httpdRestart()
		

	elif int(choice) == 2:
		print ("\nRestarting httpd...")
		print ("---------------------")
		server.httpdRestart()
		cont()
		
	elif int(choice) == 3:
		print ("\nCreate File")
		print ("--------------")		
		fname = raw_input("Input the file name with extension:")
		e_code = commands.getstatusoutput("touch" + " "+ fname)
		if int(e_code[0]) == 0:
			print(fname, " created successfully")
		else: 
			print("file creation failed")
			print("Error: ", e_code[1])
		cont()
	elif int(choice) == 4:
		print ("\nCreate user")
		print ("-----------")
		userName = raw_input("Enter username: ")
		userPasswd = getpass.getpass("Enter password for " + userName + ": ")
		e_code = commands.getstatusoutput(" sudo useradd -p " + userPasswd + " " + userName)
		if e_code[0] == 0:
			print("user ", userName ," created successfully")
			cont()
			#userPasswordStatus = commands.getstatusoutput("echo {0} | sudo passwd {1} --stdin".format(userPasswd, userName))			
		else:
			print("user \'", userName,"\' creation failed")
			print("Error: \n", e_code[1])
			
	elif int(choice) == 5:
		print ("\nMount a drive")
		print ("---------------")
		
		cont()

	elif int(choice) == 0:
		print ("Closed")
		exit()
	else:
		print ("Input valid option")
		cont()
def end():
	os.system("clear")
	exit()

def init():
	mainMenu()
	Server().Slogin()
init()
