#!/usr/bin/python
import sys
def hello(name):
	if name=='tinku' or name=='pinky':
		print'alert agent mode'
		name=name+'???'
		name=name+'!!!'
		print 'hello'+name
	
def main():
	hello(sys.argv[1])

if __name__ == '__main__':
	main()

