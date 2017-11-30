#!/usr/bin/python -tt
# Command:      python foodstock.py
# Description:  looping with pyhton dictionaries
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

prices = {
          "banana" : 4,
          "apple"  : 2,
          "orange" : 1.5,
          "pear"   : 3,
                }
stock = {
          "banana" : 6,
          "apple"  : 0,
          "orange" : 32,
          "pear"   : 15,
                }

for key in prices:
      print key
      print "price: %s" % prices[key]
      print "stock: %s" % stock[key]
            
total = 0
for key in prices:
    value = prices[key] * stock[key]
    print value
    total = total + value
                        
print total

"""
OUTPUT:

rudra@rudran:~/python$ python foodstock.py
orange
price: 1.5
stock: 32
pear
price: 3
stock: 15
banana
price: 4
stock: 6
apple
price: 2
stock: 0
48.0
45
24
0
117.0

"""
