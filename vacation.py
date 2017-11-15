#!/usr/bin/python -tt

# Command:      python vacation.py or ./vacation.py
# Description:  vacation cost calculator
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 

city = str(raw_input("Input city name:Delhi/Mumbai/Pune/Banglore: "))
days = int(input("Input number of days for vacation: "))
spending_money = int(input("Input extra money for spending: "))

def hotel_cost(days):
  return 140 * days

def plane_ride_cost(city):
  if city == "Delhi":
    return 183
  elif city == "Mumbai":
    return 220
  elif city == "Pune":
    return 222
  elif city == "Banglore":
    return 475
  
def rental_car_cost(days):
  total = 40 * days
  if days >= 7:
    total = total - 50
  elif days >= 3:
    total = total - 20
  return total

def main():
  print "Total estimated cost is: ",rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

if __name__ == "__main__":
	main()

"""
OUTPUT:

rudra@rudran:~/python$ python vacation.py 
Input city name:Delhi/Mumbai/Pune/Banglore: Pune
Input number of days for vacation: 10
Input extra money for spending: 5000
Total estimated cost is:  6972

"""
