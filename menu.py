#!/usr/bin/python2
# -*- coding: utf-8 -*-

from __future__ import print_function
import os
import commands
import getpass
import curses
import staas

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


def cont():
	raw_input ("Press enter to continue...")
	menu()
	menu_choice()

def menu():
		print (color.YELLOW + "\t\t\t\t\t- Welcome to -" + color.END )
		os.system("tput setaf 1")
		print ("""
\t8888888b.         888   888                        888b     d888                         
\t888   Y88b        888   888                        8888b   d8888                         
\t888    888        888   888                        88888b.d88888                         
\t888   d88P888  88888888888888b.  .d88b. 88888b.    888Y88888P888 .d88b. 88888b. 888  888 
\t8888888P" 888  888888   888 "88bd88""88b888 "88b   888 Y888P 888d8P  Y8b888 "88b888  888 
\t888       888  888888   888  888888  888888  888   888  Y8P  88888888888888  888888  888 
\t888       Y88b 888Y88b. 888  888Y88..88P888  888   888   "   888Y8b.    888  888Y88b 888 
\t888        "Y88888 "Y888888  888 "Y88P" 888  888   888       888 "Y8888 888  888 "Y88888 
\t             888                                                                       
\t        Y8b d88P                                                                       
\t         "Y88P"                                                                        
		""")
		os.system("tput setaf 7")
		ws = " "
		print (4*ws,"-----------------------------------------------------------------------------------------------")
		print("\n\n")
		print ("""
		Press 1: To see cal
		Press 2: To see date
		Press 3: To create file
		Press 4: To create user
		Press 5: To mount a drive
		Press 0: To exit
		""")
def menu_choice():	
	choice = int(raw_input("Enter your choice: "))
	if int(choice) == 1:
		print ("Calender: ")
		print (commands.getoutput("cal "))
		cont()

	elif int(choice) == 2:
		print ("\nDate")
		print ("-------")
		print (commands.getoutput("\ndate"))
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

menu()
menu_choice()
