#!/usr/bin/env python -tt

# Command:      ./write.py newfile.txt
# Description:  python write method
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
import sys
def cat(filename):
	f=open(filename,'w')
	for val in range(5):
		f.write(str(val)+'\n')
	f.close
	print"file operation over"
def main():
	cat(sys.argv[1])
	
if __name__ == "__main__":
	main()

"""
OUTPUT:

rudra@rudran:~/python$ touch file.txt
rudra@rudran:~/python$ python write.py file.txt 
file operation over
rudra@rudran:~/python$ cat file.txt 
0
1
2
3
4

"""
