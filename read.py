#!/usr/bin/env python -tt

# Command:      ./read.py file.txt
# Description:  python read method
# Author:       rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
import sys
def print_file(filename):
	f=open(filename,'rU')
	print"the datatype of veriable 'f' is",type(f)
	print"============================================"
	string=f.read()
	print"the datatype of variable 'string' is",type(string)
	print"=================================================="
	print repr(string)
	print"=================================================="
	print string
	f.close()
def main():
	print_file(sys.argv[1])

if __name__ == "__main__":
	main()
