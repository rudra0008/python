#!/usr/bin/env python

# Command:      python time2.py
# Description:  Converts seconds to hh:mm:ss (time formate)
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

import time
def main():
  print time.strftime('%H:%M:%S', time.gmtime(987654321))

if __name__ == "__main__":
	main()

"""
OUTPUT:

rudra@rudran:~/python$ python time2.py 
04:25:21

"""
