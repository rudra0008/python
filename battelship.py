#!/usr/bin/python -tt
# Command:      python battelship.py
# Description:  battelship game. you have to guess the location of ship
# Author:       Rudra
# Maintainer:   rudra0008
# Project:      https://github.com/rudra0008/python
# Dependencies: 
from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

print_board(board)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

"""
print ship_row
print ship_col

"""
# Everything from here on should be in for loop
# don't forget to properly indent!
for turn in range(9):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!" 
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      if turn == 8:
        print "Game Over"
      	print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)


"""
OUTPUT:

rudra@rudran:~/python$ python battelship.py 
O O O O O
O O O O O
O O O O O
O O O O O
O O O O O
3
3
Turn 1
Guess Row: 2
Guess Col: 3
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Turn 2
Guess Row: 5
Guess Col: 6
Oops, that's not even in the ocean.
O O O O O
O O O O O
O O O X O
O O O O O
O O O O O
Turn 3
Guess Row: 1
Guess Col: 2
O O O O O
O O X O O
O O O X O
O O O O O
O O O O O
Turn 4
Guess Row: 3
Guess Col: 3
Congratulations! You sank my battleship!

"""
