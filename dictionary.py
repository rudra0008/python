#!/usr/bin/env python -tt

# Command:      python dictionary.py
# Description:  use of dictionary in python
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['fried chicken'] = 20.50
menu['grilled fish'] = 10.50
menu['boiled egg'] = 0.50


print "There are " + str(len(menu)) + " items on the menu."
print menu

"""
OUTPUT:

rudra@rudran:~/python$ python dictionary.py 
14.5
There are 4 items on the menu.
{'boiled egg': 0.5, 'Chicken Alfredo': 14.5, 'grilled fish': 10.5, 'fried chicken': 20.5}

"""
