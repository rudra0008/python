#!/usr/bin/python -tt
def hello(name):
	print"program entered hello() function"
	var1="hello"+name
	print"program leaving hello() function"
	return var1
	print"this live will not be printed"

def main():
	name="tinku"
	print"program calling hello() function"
	str1=hello(name)
	print"program execution returned back to main()"
	print str1
	print"program finished execution hello() function"

if __name__ == "__main__":
	main()
