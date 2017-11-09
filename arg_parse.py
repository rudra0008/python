#!/usr/bin/env python -tt

# Command:      ./arg_parse.py -h
# Description:  python argparse module
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo", help="echo the string you use here")
args = parser.parse_args()
print args.echo

"""
OUTPUT:

rudra@rudran:~/python$ python arg_parse.py 
usage: arg_parse.py [-h] echo
arg_parse.py: error: too few arguments
rudra@rudran:~/python$ python arg_parse.py -h
usage: arg_parse.py [-h] echo

positional arguments:
  echo        echo the string you use here

optional arguments:
  -h, --help  show this help message and exit

"""
