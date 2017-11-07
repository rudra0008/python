#!/usr/bin/env python -tt

# Command:      ./fileIO file.txt
# Description:  file input output in python
# Author:       Rudra
# Maintainer:   Rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

import sys
def print_file(filename):
	f=open(filename,'rU')
	print"the datatype of variable 'f' is",type(f)
	print"===================================================="
	for line in f:
		print line
		print "the datatype of 'line' is:",type(line)
	f.close()
def main():
	print_file(sys.argv[1])
if __name__ == "__main__":
	main()

"""
OUTPUT:

rudra@rudra-ThinkPad-T430:~/python$ python fileIO.py 0argument.py 
the datatype of variable 'f' is <type 'file'>
====================================================
#!/usr/bin/python -tt

the datatype of 'line' is: <type 'str'>
#python function with zero argument

the datatype of 'line' is: <type 'str'>
def hello():

the datatype of 'line' is: <type 'str'>
	print "greetings from python!"

the datatype of 'line' is: <type 'str'>
def main():

the datatype of 'line' is: <type 'str'>
	hello()

the datatype of 'line' is: <type 'str'>
if __name__ == "__main__":

the datatype of 'line' is: <type 'str'>
	main()

the datatype of 'line' is: <type 'str'>

"""
