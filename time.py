#!/usr/bin/python -tt
# Command:      python time_hhmmss.py
# Description:  convert seconds to hh:mm:ss time formate
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
def main():
	seconds = int(input("enter time in seconds: "))
	h = seconds/3600
	hh = h%24
	s = seconds%3600
	mm = s/60
	ss = s%60
	print "the time is: ",hh,":",mm,":",ss
if __name__ == "__main__":
	main() 

"""
OUTPUT:

rudra@rudran:~/python$ python time.py 
enter time in seconds: 987654321
the time is:  4 : 25 : 21

"""
