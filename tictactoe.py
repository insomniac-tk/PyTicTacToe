'''
    Author : Tejas Khanna
    Version: 0.1
'''
from random import randint
import time
import sys

def game_header():
    print("### PyTicTacToe ###")
    print("Developed By Tejas Khanna | Version 0.1")
    print("This is the python implementation of the famous two player paper and pencil strategy game.")
    print("Feel free to use this code and modify it as you please :D ")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def display_numpad():
    print(" - "*10)
    print("\tPyTicTacToe Rules")
    print(" - "*10)
    for i in range(9,0,-3):
        k = i 
        print("\t| ({}) ({}) ({}) |".format(k-2,k-1,k))
        print()
    print(" - "*10)
    time.sleep(2)

def display(board):
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
    return p1,p2,p1_mark,p2_mark

def first_chance():
    print("Now the computer will randomly pick who starts first ")
    print("Computer is deciding",end='')
    delay_print('.'*10)
    print()
    time.sleep(5)
    coin_flip = randint(0,1)
    first_chance = 'Player 1' if coin_flip==0 else 'Player 2'
    return first_chance

def rules():
    b = ['']*10 
    #print(len(b))
    display_numpad()
    print('You have to use the numpad on your keyboard to pick the position\nwhere you would like to place your mark(X or O).')
    print('This is what an empty board looks like')
    display(b)
    time.sleep(2)
    print("Say, I wish to place an X on position 9, this is what the board will look like after that")
    place_mark('X',9,b) 
    display(b)
    time.sleep(2)

def is_board_full(board):
    return not '' in board
    # '' in board -> false
    # not false = > true

def is_winner(mark,board):
    rows = (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark)  or (board[7] == mark and board[8] == mark and board[9] == mark)
    cols = (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark)  or (board[3] == mark and board[6] == mark and board[9] == mark)
    diags = (board[1] == mark and board[5] == mark and board[9] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark)
    return rows or cols or diags

def space_check(board,position):
    return board[position] ==   ''

def input_postion(p):
    # the input position has to be an integer 
    pos = int(input('Enter your position, {}: '.format(p)))
    return pos

def main():
    board = ['']*10
    game_header()
    player1,player2,player1_mark,player2_mark = input_players()
    rules()
    game_on = True
    while game_on:
        turn = first_chance()
        print("{} will start!".format(turn))
        # Player 1
        if turn == 'Player 1':
            # First show the board to the player 
            display(board)

            # If the board isn't full let the player enter a position

            if not is_board_full(board):
                pos = 0
                while pos not in [1,2,3,4,5,6,,7,8,9] or not space_check(board,pos):
                    pos = input_postion(turn)
                place_mark(player1_mark,pos,board) 
                display(board)
            # So now what all can happen after player1 has made it's move 
            # 1. He might win.
            # 2. The board might become full 
            # 3. Nothing. We let player 2 play now.

            if is_winner(player1_mark,board):
                print('Player 1 has won!')
                game_on = False

            elif is_board_full(board):
                print('Game is a draw.')
                game_on = False

            else:
                turn = 'Player 2'
        else:
            
            display(board)

            if not is_board_full(board):
                pos = 0
                while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
                    pos = input_postion(turn)
                place_mark(player2_mark,pos,board) 
                display(board)
       

            if is_winner(player1_mark,board):
                print('Player 1 has won!')
                game_on = False

            elif is_board_full(board):
                print('Game is a draw.')
                game_on = False

            else:
                turn = 'Player 1'




if __name__=='__main__':
    main()