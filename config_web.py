import commands,os

'''userName  = raw_input("Enter user name: ")

userPass = raw_input("Enter Password: ")

userIP = raw_input("Enter IP: ")'''


	
userName = "root"
userPass = "redhat"
userIP = "192.168.43.33"

SSHLogin = "sshpass -p {0} ssh -o stricthostkeychecking=no -l {1} {2}".format(userPass, userName, userIP)

firewall = SSHLogin + " systemctl stop firewalld"
firewallF = commands.getstatusoutput(firewall)
if(firewallF[0] == 0):
	print(firewallF[1])
else:
	print(firewallF[1])
	
#print(SSHLogin)
#login = commands.getstatusuoutput(SSHLogi)

#portNumber = raw_input("Enter port number: ")
#documentRoot = raw_input("Enter DocumentRoot: ")

portNumber = '12345'
documentRoot = '/abhi'

configFile = "{0}.conf".format(userName)
fp = open(configFile, 'w')
fp.write("Listen {0}\n".format(portNumber))
fp.write('DocumentRoot "{0}"\n'.format(documentRoot))
fp.write('<Directory "{0}">\n\tRequire all granted\n</Directory>\n'.format(documentRoot))
fp.close()

#configData = 'Listen {0}\n\n DocumentRoot "{1}"\n\n <Directory "{1}">\n\tRequire all granted\n</Directory>\n'.format(portNumber, documentRoot)

fileTransfer = "scp {0} {1}@{2}:/etc/httpd/conf.d/".format(configFile, userName, userIP)
fileF = commands.getstatusoutput(fileTransfer)
if(fileF[0] == 0):
	print(fileF[1])
else:
	print(fileF[1])

#fileWrite = SSHLogin + " echo '{0}' | cat >> /etc/httpd/conf.d/{1}".format(configData, configFile)
#print(fileWrite)
#commands.getstatusoutput(fileWrite)
	

httpd =  SSHLogin + " systemctl restart httpd"
SELinux = SSHLogin + " setenforce 0"

SELinuxF = commands.getstatusoutput(SELinux)
if(SELinuxF[0] == 0):
	print("SELinux stopped.")
else:
	print("Cannot stop SELinux.")
	

httpdF = commands.getstatusoutput(httpd)
if(httpdF[0] == 0):
	print(httpdF[1])
else:
	print(httpdF[1])
