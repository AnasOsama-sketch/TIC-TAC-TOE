import turtle
turtle = turtle.Turtle(shape='turtle')

from random import randint

turtle.speed(0)

board = [['empty' for row in range(3)] for column in range(3)]
turn = randint(1, 2)
row = 1
change_turn = 0
column = 1
x = -197
y = -194

#These functions declare who is the winner.
def x_won():
    turtle.clear()
    turtle.color('blue')
    turtle.setposition(-10, 0)
    turtle.write('X Won!', align = 'center', font = ('Arial', 75, 'bold'))
    turtle.color('white')
def o_won():
    turtle.clear()
    turtle.color('red')
    turtle.setposition(-10, 0)
    turtle.write('O Won!', align = 'center', font = ('Arial', 75, 'bold'))
    turtle.color('white')
def draw_check():
    if(board[0][0] != 'empty' and board[0][1] != 'empty' and board[0][2] != 'empty' and win_check() == 0):
        if(board[1][0] != 'empty' and board[1][1] != 'empty' and board[1][2] != 'empty' and win_check() == 0):
            if(board[2][0] != 'empty' and board[2][1] != 'empty' and board[2][2] != 'empty' and win_check() == 0):
                condition_draw()
                return 1
"""
The following Function creates a square with the side length 130px
at the current position.
"""
def draw_square():
    turtle.pendown()
    for i in range(4):
        turtle.forward(130)
        turtle.left(90)

#The following function checks who won.
def win_check():
    for i in range(3):
        if(board[i][0] == board[i][1] == board[i][2] and board[i][0] == 'x'):
            x_won()
            return 1
        elif(board[i][0] == board[i][1] == board[i][2] and board[i][0] == 'o'):
            o_won()
            return 2
        elif(board[0][i] == board[1][i] == board[2][i] and board[0][i] == 'x'):
            x_won()
            return 1
        elif(board[0][i] == board[1][i] == board[2][i] and board[0][i] == 'o'):
            o_won()
            return 2
    if(board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'x'):
        x_won()
        return 1
    elif(board[0][0] == board[1][1] == board[2][2] and board[0][0] == 'o'):
        o_won()
        return 2
    elif(board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'x'):
        x_won()
        return 1
    elif(board[0][2] == board[1][1] == board[2][0] and board[0][2] == 'o'):
        o_won()
        return 2
    else:
        return 0

#This function checks if the current condition is draw (tie).
def condition_draw():
    turtle.clear()
    turtle.color('Purple')
    turtle.setposition(-10, 0)
    turtle.write('Draw!', align = 'center', font = ('Arial', 75, 'bold'))
    turtle.color('white')

#This function creates the 3 by 3 grid for the TIC TAC TOE game.
def create_grid(x, y):
    for l in range(3):
        turtle.penup()
        turtle.setposition(x, y)
        for i in range(3):
            draw_square()
            turtle.forward(130)
        y += 130

"""
The following function checks the movement for player 1 and 2, and
contains the loop of the game.
"""
def game_loop(row, column, turn):
    x = 0
    y = 0
    prevX = x
    prevY = y
    while True:
        if(win_check() != 0 or draw_check() == 1 ):
            turtle.setposition(-200, -200)
            break
        win_check()
        draw_check()
        turtle.penup()
        turtle.setposition(x, y)

        if(turn == 1):
            print('>> The move is for player 1')
        else:
            print('>> The move is for player 2')

        c = input('>> Enter your command: ')
        if(turn == 1):
            if(c == 'w'):
                y = min(130, y + 130)
                if(prevY != y):
                    row -= 1
            elif(c == 's'):
                y = max(-130, y - 130)
                if(prevY != y):
                    row += 1
            elif(c == 'a'):
                x = max(-130, x - 130)
                if(prevX != x):
                    column -= 1
            elif(c == 'd'):
                x = min(130, x + 130)
                if(prevX != x):
                    column += 1
            elif(c == 'X' or c == 'draw' or c == 'x'):
                turtle.setposition(x, y-20)
                if(board[row][column] == 'empty'):
                    turtle.color('blue')
                    turtle.write('X', align = 'center', font = ('Arial', 40, 'bold'))
                    board[row][column] = 'x'
                    turtle.color('black')
                    turtle.setposition(x, y)
                    turn = 2
                else:
                    print(">> You have already placed " + board[row][column] + " here!")
        elif(turn == 2):
            if(c == 'i'):
                y = min(130, y + 130)
                if(prevY != y):
                    row -= 1
            elif(c == 'k'):
                y = max(-130, y - 130)
                if(prevY != y):
                    row += 1
            elif(c == 'j'):
                x = max(-130, x - 130)
                if(prevX != x):
                    column -= 1
            elif(c == 'l'):
                x = min(130, x + 130)
                if(prevX != x):
                    column += 1
            elif(c == 'O' or c == 'draw' or c == 'o'):
                turtle.setposition(x, y-20)
                if(board[row][column] == 'empty'):
                    turtle.color('red')
                    turtle.write('O', align = 'center', font = ('Arial', 40, 'bold'))
                    board[row][column] = 'o'
                    turtle.color('black')
                    turtle.setposition(x, y)
                    turn = 1
                else:
                    print(">> You have already placed " + board[row][column] + " here!")
                
        else:
            print(">> Command unkown!")
        #print board
        prevX = x
        prevY = y
            
create_grid(x, y)
game_loop(row, column, turn)