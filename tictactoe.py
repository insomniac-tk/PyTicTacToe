from os import system,name
from time import sleep 

# Some globals
players = {}
players['p1_move'] = 'X'
players['p2_move'] = 'O'

GameOver = False
initial_board = [[1,2,3],[4,5,6],[7,8,9]]

def board(l=initial_board):
    global GameOver
    for i in l:
        if i == ['X']*3 or i == ['O']*3:
            GameOver = True
    return GameOver

def hr():
    print('=====================================')


def startup():
    system('clear')
    print("\t############# PyTicTactToe v1.0 #############\n\t --------------------------------------")
    p1 = input('Enter Player 1 Name - ')
    p2 = input('Enter Player 2 Name - ')
    players['p1'] = p1
    players['p2'] = p2
    print('Welcome  {} and {}! May the best player win!'.format(players['p1'],players['p2']))
    hr()
    print('{} moves first'.format(players['p1']))
    print('{} = X and {} = O'.format(players['p1'],players['p2']))
    print("Let's begin")
    board()
    #game()


def game():
    while GameOver == False:
        pos  = input('{} , enter the postion where you want to put an X >> '.format(players['p1']))
          
l = [[1,2,3],[4,5,6],['X','X','X']]
print(board(l))
print(GameOver)
#startup()