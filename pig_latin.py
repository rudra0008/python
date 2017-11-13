#!/usr/bin/python -tt
# Command:      python pig_latin.py
# Description:  pig latin translator.
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print new_word
else:
  print 'empty'

"""
Pig Latin is a language game, where you move the first letter of the word to the end and add "ay".
So "Python" becomes "ythonpay".

OUTPUT:

rudra@rudran:~/python$ python pig_latin.py 
Enter a word:python
ythonpay

"""
