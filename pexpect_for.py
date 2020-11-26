#!/usr/bin/env python3
#-*- encoding utf-8 -*-
import pexpect

# Set the connection

def main():

	# commands to test: [ ls -alh  pwd  uname -a ]

	a = ['uname -a', 'pwd', 'ls -alh']
	pexpect.sys.stdout = open('/tmp/logOutput', 'a+') #this is for log the stdout from the executed commands
	
	c = pexpect.spawn('ssh tenex@127.0.0.1', timeout=None)#, logfile=pexpect.sys.stdout)
	c.expect ('password:')
	c.sendline('hackmaster')
	#time.sleep(1)
	#c.logfile = pexpect.sys.stdout
	for cmd in a:
		#pexpect.run(cmd)
		#c.logfile = pexpect.sys.stdout
		#pexpect.spawnu(cmd, timeout=1)
		o = pexpect.run(cmd, timeout=None)
		print(o)
		#print(o)
		#print(f"reading:\n{c.readline()}")
		#print(c.before, c.after)
		#c.expect(pexpect.EOF)
		c.expect(["$"])#, pexpect.EOF, pexpect.TIMEOUT])
		
		#print(c.before, c.after)
			

	c.close()
	#c.sendline("exit")
	#c.close(force=True)
	#c.logfile.close()
	#print("check the log")

if __name__ == '__main__':
	main()