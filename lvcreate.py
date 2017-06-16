#!/usr/bin/python2

import commands

userName = raw_input ("Enter name of user: ")
driveSize = raw_input("Enter drive size in GBzzzzs: ")

createPart = "lvcreate --size {0}G --name {1} vg1".format(driveSize, userName)

driveCreateStatus = commands.getstatusoutput(createpart)
if driveCreateStatus[0] == 0:
	print "drive create successfully..."
	commands.getstatusoutput("mkfs.ext4 /dev/vg1/{}".format(userName))

	commands.getstatusoutput("mkdir -p /cloud/myLV1")

	commands.getstatusoutput("mount /dev/vg1/myLV1 /cloud/myLV1")

	commands.getstatusoutput("echo '/cloud/myLV1	*(rw,no_root_squash)' >> /etc/exports")
	commands.getstatusoutput("systemctl restart nfs")

else:
	print "Drive not created..."


raw_input("Enter to close...")
