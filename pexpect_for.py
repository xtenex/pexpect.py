#!/usr/bin/env python3
#-*- encoding utf-8 -*-
import pexpect

# Simple pexpect example to execute multiple commands in python 3
# If you want to make it interact then import sys module and use sys.argv to get from CLI
# An issue that i don't know how to solve is the logging funciton is on binary and the strings starts with b'[string]

def main():

	# commands to test: [ ls -alh  pwd  uname -a ]

	a = ['uname -a', 'pwd', 'ls -alh'] # Add here your command list
	pexpect.sys.stdout = open('/tmp/logOutput', 'a+') #this is to log the stdout from the executed commands
	
	c = pexpect.spawn('ssh user@127.0.0.1', timeout=None) # This is to connect to the server, if you want to insert it then add sys.argv[x]
	c.expect ('password:')
	c.sendline('MyPassword')
	#c.logfile = pexpect.sys.stdout # This is useless, is not working don't use it
	for cmd in a:
		o = pexpect.run(cmd, timeout=None)
		print(o)
		c.expect(["$"])
		#print(c.before, c.after) # this is not necessary that's why is commented

	c.close()
if __name__ == '__main__':
	main()
