#!/usr/bin/python2

import commands

driveName = raw_input("Enter your drive name: ")
mountPointCreator = commands.getstatusoutput("sudo mkdir /media/" + driveName)

if mountPointCreator[0] == 0:
	print ("directory mount successful")

shareMount = commands.getstatusoutput("sudo mount 192.168.43.33:/ram /media/" + driveName)

if shareMount[0] == 0:
	print ("Drive created")
	removeDrive = raw_input ("Press 'q' to unmount '" + driveName + "'\n")
	if removeDrive == "q":
		commands.getstatusoutput("sudo umount /media/" + driveName)
		raw_input("Successfully removed. Press enter to close...")
	else:
		print ("Option not supported")
else:
	print ("Drive not created...")


