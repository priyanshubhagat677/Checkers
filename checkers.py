from rich.console import Console
from rich.table import Table
import os

#The initial board in it's starting position

main = [
    ['#','1','2','3','4','5','6','7','8'],
    ['1',' ','O',' ','O',' ','O',' ','O'],
    ['2','O',' ','O',' ','O',' ','O',' '],
    ['3',' ','O',' ','O',' ','O',' ','O'],
    ['4',' ',' ',' ',' ',' ',' ',' ',' '],
    ['5',' ',' ',' ',' ',' ',' ',' ',' '],
    ['6','X',' ','X',' ','X',' ','X',' '],
    ['7',' ','X',' ','X',' ','X',' ','X'],
    ['8','X',' ','X',' ','X',' ','X',' '],
]

#switches player's turn
turn =-1

while True:

    os.system('cls')

    # to display on top of the table
    if turn == -1:
        turnstr = 'X\'s turn'
    else:
        turnstr = 'O\'s turn'

    #initializing the table
    board = Table(title='Board:'+turnstr, show_lines=True, show_header=False)

    #displaying the table
    for i in main:
        board.add_row(*i)
    Console().print(board)


    print("From:To")
    initial_x,initial_y = map(int,input().split(','))


    possible_moves= [[initial_x+1,initial_y+1],[initial_x+1,initial_y-1],
                     [initial_x-1,initial_y+1],[initial_x-1,initial_y-1]]


    final_x,final_y = map(int,input().split(','))

    '''
        checking whether captures are possible by checking the values in the 
        two diagonal consecutive coordinates 
    '''

    if turn== -1: #X's turn

        if (main[initial_y-1][initial_x+1]== 'O') and (main[initial_y-2][initial_x+2]==' 'and main[initial_y][initial_x] == 'X'):
            if((final_x==initial_x+2)and(final_y==initial_y-2)):
                main[final_y][final_x]='X'
                main[initial_y][initial_x]=' '
                main[initial_y-1][initial_x+1] = ' '
                turn *= -1

                continue

        if (main[initial_y-1][initial_x-1]== 'O') and (main[initial_y-2][initial_x-2]==' 'and main[initial_y][initial_x] == 'X'):
            if((final_x==initial_x-2)and(final_y==initial_y-2)):
                main[final_y][final_x]='X'
                main[initial_y][initial_x]=' '
                main[initial_y - 1][initial_x - 1] = ' '
                turn *= -1

                continue

    if turn == 1:  # O's turn

        if (main[initial_y + 1][initial_x + 1] == 'X') and (main[initial_y + 2][initial_x + 2] == ' 'and main[initial_y][initial_x] == 'O'):
            if ((final_x == initial_x + 2) and (final_y == initial_y + 2)):
                main[final_y][final_x] = 'O'
                main[initial_y][initial_x] = ' '
                main[initial_y + 1][initial_x + 1] = ' '
                turn *= -1

                continue

        if (main[initial_y + 1][initial_x - 1] == 'X') and (main[initial_y + 2][initial_x - 2] == ' 'and main[initial_y][initial_x] == 'O'):
            if ((final_x == initial_x - 2) and (final_y == initial_y + 2)):
                main[final_y][final_x] = 'O'
                main[initial_y][initial_x] = ' '
                main[initial_y + 1][initial_x - 1] = ' '
                turn *= -1

                continue


    #check move validity

    if [final_x,final_y] not in possible_moves:
        continue

    if main[final_y][final_x] != ' ':
        continue


    #for moving on empty squares
    if (turn == -1) and (main[initial_y][initial_x]=='X'):
        main[final_y][final_x]='X'
        turn *= -1
        main[initial_y][initial_x] = ' '

    elif (turn == 1) and (main[initial_y][initial_x]=='O'):
        main[final_y][final_x] = 'O'
        turn *= -1
        main[initial_y][initial_x] = ' '