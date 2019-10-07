'''
	Author : Tejas Khanna

'''
from random import randint
import time
import sys

def game_header():
	print("### PyTicTacToe ###")
	print("Developed By Tejas Khanna | Version 0.1")
	print(" This is the python implementation of the famous two player paper and pencil strategy game.")
	print("Feel free to use this code and modify it as you please :D ")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def display_numpad():
	print(" - "*10)
	print("\tPyTicTacToe")
	print(" - "*10)
	for i in range(9,0,-3):
		k = i 
		print("\t| ({}) ({}) ({}) |".format(k-2,k-1,k))
		print()
	print(" - "*10)

def display(board):
	print(" - "*10)
	print("\tPyTicTacToe")
	print(" - "*10)
	for i in range(9,0,-3):
		k = i 
		print("\t| ({}) ({}) ({}) |".format(board[k-2],board[k-1],board[k]))
		print()
	print(" - "*10)

def place_mark(mark,position,board):
	board[position] = mark

def input_players():
	p1 = input("Enter your name player 1: ")
	p2 = input("Enter your name player 2: ")
	print("Welcome on board {} and {}".format(p1,p2))
	tmp = ''
	while not(tmp=='X' or tmp=='O'):
		tmp = input("Choose your mark player1(X or O) => ")
	p1_mark = tmp
	p2_mark = 'X' if p1_mark == 'O' else 'O'
	print("{}: {},{} : {}".format(p1,p1_mark,p2,p2_mark))
	
	print("Now the computer will randomly pick who starts first ")
	print("Computer is deciding",end='')
	delay_print('.'*10)
	print()
	time.sleep(5)
	coin_flip = randint(0,1)
	first_chance = coin_flip 

	if coin_flip == 1:
		print('{} will start'.format(p1))
	else:
		print('{} will start'.format(p2))

	print("All the best {} & {} for the game...!".format(p1,p2))


def rules():
	b = ['']*10	
	#print(len(b))
	display_numpad()
	print('You have to use the numpad on your keyboard to pick the position\nwhere you would like to place your mark(X or O).')
	print('This is what an empty board looks like')
	display(b)
	print("Say, I wish to place an X on position 9, this is what the board will look like after that")
	place_mark('X',9,b)	
	display(b)

