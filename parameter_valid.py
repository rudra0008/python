#!/usr/bin/python -tt
import sys
def main():
	if len(sys.argv)==3:
		fn=sys.argv[1]
		ln=sys.argv[2]
		print fn
		print ln
	else:
		print "exact two parameters required"

if __name__ == "__main__":
	main()
