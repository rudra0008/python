#!/usr/bin/env python -tt

# Command:      ./readline.py file.txt
# Description:  python readlines method
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

import sys
def print_file(filename):
	f=open(filename,'rU')
	print "the datatype of variable 'f' is",type(f)
	print"==================================================="
	lines=f.readlines()
	print"the datatype of variable 'lines' is",type(lines)
	print"==================================================="
	print lines
	print "=================================================="
	for line in lines:
		print line
		print type(line)
	f.close
def main():
	print_file(sys.argv[1])
if __name__ == "__main__":
	main()	

"""
OUTPUT:

rudra@rudra-ThinkPad-T430:~/python$ python readline.py hello.py 
the datatype of variable 'f' is <type 'file'>
===================================================
the datatype of variable 'lines' is <type 'list'>
===================================================
['#!/usr/bin/python -tt\n', '#define the main() function that prints Hello world\n', 'def main():\n', "\tprint 'Hello world'\n", '#standard boiler plate syntax that calls the main() function.\n', '\n', "if __name__ == '__main__':\n", '\tmain()\n', '\n']
==================================================
#!/usr/bin/python -tt

<type 'str'>
#define the main() function that prints Hello world

<type 'str'>
def main():

<type 'str'>
	print 'Hello world'

<type 'str'>
#standard boiler plate syntax that calls the main() function.

<type 'str'>


<type 'str'>
if __name__ == '__main__':

<type 'str'>
	main()

<type 'str'>


<type 'str'>

"""
