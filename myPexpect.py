#!/usr/bin/env python3.9
#-*- encode: utf-8 -*-

import pexpect

def main():

	#comands = ['ls -alh', 'pwd', 'uname -a']
	#hn = "/tmp/" + pexpect.sys.argv[1]

	#pexpect.sys.stdout = open(hn, "a+")

	c = pexpect.spawn('ssh user@127.0.0.1', encoding='utf-8', timeout=5, logfile=pexpect.sys.stdout)
	#print(f"valor de c: {c}\ntipo de c:{type(c)}")
	index = c.expect(["connecting", "password", "$", pexpect.EOF, pexpect.TIMEOUT])
	if index == 0:
		c.sendline('yes')
		c.expect("password")
		c.sendline('MyPassword')
		loops(c)

	elif index == 1:
		c.sendline('MyPassword')
		c.expect(["$","#"])
		loops(c)

	elif index == 2:
		loops(c)

	elif index == 3:
		print("The child has exited and EOF error was raised")
		

	elif index == 4:
		print("Timeout... An exception was raised")
		#break


def loops(fn):

	comands = ['ls -alh', 'pwd', 'uname -a']
	#fn.expect(["$", "#"])
	hn = "/tmp/" + "logfile" + ".txt"
	pexpect.sys.stdout = open(hn, "a+")
	for cmd in comands:
		o = pexpect.run(cmd, timeout=None)
		print(o)
		fn.expect(["$","#"])

	pexpect.sys.stdout.close()


if __name__ == '__main__':
	main()
