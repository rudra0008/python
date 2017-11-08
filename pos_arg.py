#!/usr/bin/env python -tt

# Command:      python pos_arg.py -h
# Description:  python argparse module
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("echo")
args = parser.parse_args()
print args.echo

"""
OUTPUT:

rudra@rudran:~/python$ python pos_arg.py 
usage: pos_arg.py [-h] echo
pos_arg.py: error: too few arguments

"""
