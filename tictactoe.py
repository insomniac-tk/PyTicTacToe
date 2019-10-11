'''
    Author : Tejas Khanna
    Version: 0.1
'''
from random import randint
import time
import os,sys

def game_header():
    print("\n\t\t\t\t\t\t### PyTicTacToe \tVersion 0.1 ###")
    print("\t\t\t\tThis is the python implementation of the famous two player paper and pencil strategy game.")
    print("\t\t\t\tFeel free to use this code and modify it as you please :D ")

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.25)

def display_numpad():
    print("\n"*3)
    print("\tPyTicTacToe Rules")
    print(" - "*10)
    for i in range(9,0,-3):
        k = i 
        print("\t| ({}) ({}) ({}) |".format(k-2,k-1,k))
        print()
    print(" - "*10)
    time.sleep(2)

def display(board):
    os.system('clear')
    print(" - "*10)
    for i in range(9,0,-3):
        k = i 
        print("\t| ( {} ) ( {} ) ( {} ) |".format(board[k-2],board[k-1],board[k]))
        print()
    print(" - "*10)

def place_mark(mark,position,board):
    board[position] = mark

def input_players():
    print('\n'*2)
    p1 = input("Enter your name player 1: ")
    p2 = input("Enter your name player 2: ")
    print("Welcome on board {} and {}".format(p1,p2))
    tmp = ''
    while not(tmp=='X' or tmp=='O'):
        tmp = input("Choose your mark {}(X or O) => ".format(p1))
    p1_mark = tmp
    p2_mark = 'X' if p1_mark == 'O' else 'O'
    print("{}: {},{} : {}".format(p1,p1_mark,p2,p2_mark))
    return p1,p2,p1_mark,p2_mark

def first_chance():
    print("Now the computer will randomly pick who starts first ")
    print("Computer is deciding",end='')
    delay_print('.'*10)
    print()
    time.sleep(1)
    coin_flip = randint(0,1)
    return 'Player 1' if coin_flip==0 else 'Player 2'

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
    return not '' in board[1:]

def is_winner(mark,board):
    rows = (board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark)  or (board[7] == mark and board[8] == mark and board[9] == mark)
    cols = (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark)  or (board[3] == mark and board[6] == mark and board[9] == mark)
    diags = (board[1] == mark and board[5] == mark and board[9] == mark) or (board[7] == mark and board[5] == mark and board[3] == mark)
    return rows or cols or diags

def is_spot_empty(board,position):
    '''
        True -  If the board[position] is empty 
        False - If the board[position] is non-empty.
    '''
    return  board[position] ==   ''
        

def input_postion(p,board):
    position = 0
    while position not in range(1,10) or not is_spot_empty(board,position):
        try:
            position = int(input('Enter your position, {}: '.format(p)))
        except ValueError:
            print('It has to be a number. Try again please :D')
        except IndexError:
            print('Whoa, that went out of bouds! Try again please :D ')
        
    
    return position

def replay():
    return input("Do you wanna play again ?").lower()=='y'
def main():
    board = ['']*10
    game_header()
    player1,player2,player1_mark,player2_mark = input_players()
    game_on = True
    turn = first_chance()
    if turn.split()[1] == '1':
        print("\n{} will start!".format(player1))
    else:
        print("\n{} will start!".format(player1)) 
    input("Hit enter to start the game!")

    while game_on:
        # Player 1
        display(board)
        #print(is_board_full(board))
        if turn == 'Player 1':
            pos = input_postion(turn,board)
            place_mark(player1_mark,pos,board) 
            display(board)
            
            # So now what all can happen after player1 has made it's move 
            # 1. He might win.
            # 2. The board might become full 
            # 3. Nothing. We let player 2 play now.

            if is_winner(player1_mark,board):
                print('{}({}) has won!'.format(player1,player1_mark))
                game_on = False

            elif is_board_full(board):
                print('Game is a draw.')
                game_on = False

            else:
                turn = 'Player 2'
        else:
            
            pos = input_postion(turn,board)
            place_mark(player2_mark,pos,board) 
            display(board)
            
            if is_winner(player2_mark,board):
                print('{}({}) has won!'.format(player2,player2_mark))
                game_on = False
                break

            elif is_board_full(board):
                print('Game is a draw.')
                game_on = False
                break

            else:
                turn = 'Player 1'



if __name__=='__main__':
    os.system('clear')
    while True:
        main()
        if not replay():
            break
