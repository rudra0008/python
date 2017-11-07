#!/usr/bin/env python -tt

# Command:      ./calculate.py or python calculate.py
# Description:  calculator
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies:

def add(a,b):
	return a + b
def sub(a,b):
	return a - b
def mul(a,b):
	return a * b
def div(a,b):
	return a / b

print("Salect Operations:")
print("1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")

choice = input("Enter your choice(1/2/3/4):") 

a=int(input("Input first number: "))
b=int(input("Input second number: "))


if choice == 1:
	print a,"+",b,"=" ,add(a,b)
elif choice == 2:
	print a,"-",b,"=" ,sub(a,b)
elif choice == 3:
	print a,"*",b,"=" ,mul(a,b)
elif choice == 4:
	print a,"/",b,"=" ,div(a,b)
else:
	print("invalid input")


'''
OUTPUT:

CASE1:

Salect Operations:
1.Addition
2.Substraction
3.Multiplication
4.Division
Enter your choice(1/2/3/4):1
Input first number: 1
Input second number: 12
1 + 12 = 13 

CASE2:

Salect Operations:
1.Addition
2.Substraction
3.Multiplication
4.Division
Enter your choice(1/2/3/4):2
Input first number: 254
Input second number: 1
254 - 1 = 253


CASE3:

Salect Operations:
1.Addition
2.Substraction
3.Multiplication
4.Division
Enter your choice(1/2/3/4):3
Input first number: 2
Input second number: 5
2 * 5 = 10


CASE4:

Salect Operations:
1.Addition
2.Substraction
3.Multiplication
4.Division
Enter your choice(1/2/3/4):4
Input first number: 10
Input second number: 2
10 / 2 = 5

CASE5:

Salect Operations:
1.Addition
2.Substraction
3.Multiplication
4.Division
Enter your choice(1/2/3/4):5
Input first number: 45
Input second number: 45
invalid input

'''
