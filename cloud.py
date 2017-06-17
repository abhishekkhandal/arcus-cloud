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
		raw_input ("\nPress enter to continue...")
		commands.getstatusoutput("clear")
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

def get_distro() :

	if [ -f /etc/redhat-release ]:
		OS="centos"
		OS_VER=commands.getstatusoutput("cat /etc/redhat-release | sed 's/Linux\ //g' | cut -d" " -f3 | cut -d. -f1")

	elif [ -f /etc/lsb-release ]:
		commands.getstatusoutput(". /etc/lsb-release")
		OS=DISTRIB_ID
		OS_VER=DISTRIB_CODENAME

	elif [ -f /etc/debian_version ]:
		commands.getstatusoutput(". /etc/os-release")
		OS="debian"  # XXX or Ubuntu??
		OS_VER=VERSION_ID
	

	#export OS=OS
	#export OS_VER=OS_VER
	#export ARCH=ARCH
	#export T_ARCH=T_ARCH
	#export WK_ARCH=WK_ARCH
	#echo Installing for OS OS_VER ARCH
	#echo

def cont():
	raw_input ("Press enter to continue...")
	mainMenu()
	menu_choice()

def mainMenu():
		print (color.YELLOW + "\t\t\t\t\t-  -" + color.END )
		os.system("tput setaf 4")
		print ("""
\t.d88888b                                                   a88888b.                   .8888b oo          
\t88.    "'                                                 d8'   `88                   88   "             
\t`Y88888b. .d8888b. 88d888b. dP   .dP .d8888b. 88d888b.    88        .d8888b. 88d888b. 88aaa  dP .d8888b. 
\t      `8b 88ooood8 88'  `88 88   d8' 88ooood8 88'  `88    88        88'  `88 88'  `88 88     88 88'  `88 
\td8'   .8P 88.  ... 88       88 .88'  88.  ... 88          Y8.   .88 88.  .88 88    88 88     88 88.  .88 
\t Y88888P  `88888P' dP       8888P'   `88888P' dP           Y88888P' `88888P' dP    dP dP     dP `8888P88 
\t                                                                                                     .88 
\t                                                                                                 d8888P  
		""")
		os.system("tput setaf 7")
		ws = " "
		print (4*ws,"-----------------------------------------------------------------------------------------------")
		print("\n\n")
		print ("""
		Log-in to remote server required:


		""")
		


def optionsMenu():
	print ("""
		Press 1: To restart server
		Press 2: To create file
		Press 3: To create user
		Press 4: To mount a drive
		Press 0: To exit
		""")
def print_line():
        print '-----------------------------'

def check_httpd():
        if 'httpd' in output:
                print_line()
                print 'Service HTTPD is running !'
                print_line()
        else:
                print_line()
                print 'Service HTTPD is not running, so starting it !'
                print_line()
                os.system('sudo systemctl start httpd')
                print 'Checking status after starting service...'
                os.system('sudo systemctl status httpd')

def check_sshd():
        if 'sshd' in output:
                print_line()
                print 'Service sshd is running !'
                print_line()
        else:
                print_line()
                print 'Service sshd is not running, so starting it !'
                print_line()
                os.system('sudo systemctl start sshd')
                print 'Checking status after starting service...'
                os.system('sudo systemctl status sshd')

def services():
        check_httpd()
        check_sshd()

def install_apache():
    print("installing apache server")
    os.system('sudo yum -y install httpd')


    print("enabling apache server")
    os.system('sudo systemctl enable httpd.service')

    print("starting apache server")
    os.system('sudo systemctl start httpd.service')

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



@task
def full_deploy():
	execute(deploy_files)
	execute(start_node)
	execute(cleanup)

@task
def start_node():
	sudo("systemctl restart nginx.service")
	sudo("systemctl restart httpd.service")
	sudo("systemctl enable /srv/node-test/node-test.service")
	sudo("systemctl restart node-test.service")

@task
def deploy_files():
	with cd("/tmp"):
		run("rm -rf /tmp/node-test")
		run('ls')
		run("git clone " + repo)
		run("ls node-test/src/")
		sudo("cp node-test/src/node-test.{js,service} " + dest_directory)
		sudo("cp node-test/src/node-test-nginx.conf /etc/nginx/conf.d/")
		sudo("cp node-test/src/node-test-apache.conf /etc/httpd/conf.d/")

@task
def cleanup():
	run("rm -rf /tmp/node-test")