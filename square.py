#!/usr/bin/env python -tt

# Command:      ./square.py <any integer number>
# Description:  print square of given number
# Author:       rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("square",help="display a square of a given number",type=int)
args = parser.parse_args()
print args.square**2

"""
OUTPUT:

rudra@rudran:~/python$ python square.py 50
2500

"""
