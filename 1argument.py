#!/usr/bin/python --tt
def hello(name):
	print "program entered hello() function"
	print "hello "+name
	print "program leaving hello() function"
	
def main():
	name="tinku"
	print "program calling hello() function"
	hello(name)
	print"program finished executing hello() function"

if __name__ == "__main__":
	main()

