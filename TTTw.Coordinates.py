from tkinter import *

#create a board
#create 2 players
#bind click and action
#make it so that each player can only have 1 turn
#make it so that a player can win


window = Tk ()
window.title("TicTacToe")
window.geometry ("800x800")

canvas_height = 400
canvas_width = 400
canvas_colour = "green"

canvas = Canvas(window, bg=canvas_colour, height=canvas_height, width = canvas_width)
canvas.pack()
canvas.create_line(150, 50, 150, 350) 
canvas.create_line(250, 50, 250, 350)
canvas.create_line(50, 150, 350, 150)
canvas.create_line(50, 250, 350, 250)


p1moves=0
currentgo='player1'
#player="0"

N = False
S = False
W = False
E = False
NW = False
NE = False
SW = False
SE = False
C = False


def p1_move_NW (self):
    global p1_y
    global currentgo
    global NW
    if currentgo == 'player1'and NW == False:
        canvas.create_line(70,70, 130, 130)
        canvas.create_line(130,70, 70, 130)
        currentgo = 'player2'
        NW = True
    else:
        print("error: It is the turn of player2")
    

def p1_move_N(Self):
    global p1_y
    global currentgo
    global N
    if currentgo == 'player1'and N == False:
        canvas.create_line(170,70,230,130)
        canvas.create_line(230,70,170,130)
        currentgo = 'player2'
        N = True
    else:
        print("error: It is the turn of player2")

def p1_move_NE(self):
    global p1_y
    global currentgo
    global NE
    if currentgo == 'player1' and NE == False:
        canvas.create_line(270,70,330,130)
        canvas.create_line(330,70,270,130)
        currentgo = 'player2'
        NE = True
    else:
        print("error: It is the turn of player2")
    

def p1_move_W(self):
    global p1_y
    global currentgo
    global W
    if currentgo == 'player1'and W == False:
        canvas.create_line(70,170, 130, 230)
        canvas.create_line(130,170,70,230)
        currentgo = 'player2'
        W = True
    else:
        print("error: It is the turn of player2")

def p1_move_SW(self):
    global p1_y
    global currentgo
    global SW
    if currentgo == 'player1' and SW == False:
        canvas.create_line(70,270,130,330)
        canvas.create_line(130,270,70,330)
        currentgo = 'player2'
        SW = True
    else:
        print("error: It is the turn of player2")

def p1_move_S(self):
    global p1_y
    global currentgo
    global S
    if currentgo == 'player1' and S == False:
        canvas.create_line(170,270,230,330)
        canvas.create_line(230,270,170,330)
        currentgo = 'player2'
        S = True
    else:
        print("error: It is the turn of player2")


def p1_move_SE(self):
    global p1_y
    global currentgo
    global SE
    if currentgo == 'player1' and SE == False:
        canvas.create_line(270,270,330,330)
        canvas.create_line(330,270,270,330)
        currentgo = 'player2'
        SE = True
    else:
        print("error: It is the turn of player2")


def p1_move_E(self):
    global p1_y
    global currentgo
    global E
    if currentgo == 'player1' and E == False:
        canvas.create_line(270,170,330,230)
        canvas.create_line(330,170,270,230)
        currentgo = 'player2'
        E = True
    else:
        print("error: It is the turn of player2")

def p1_move_C(self):
    global p1_y
    global currentgo
    global C
    if currentgo == 'player1'and C == False:
        canvas.create_line(170,170,230,230)
        canvas.create_line(230,170,170,230)
        currentgo = 'player2'
        C = True
    else:
        print("error: It is the turn of player2")


#def callback(event):
#    event.x, event.y 


#window.bind("<Button-1>", callback)

window.bind("i", p1_move_NW)
window.bind("o", p1_move_N)
window.bind("p", p1_move_NE)
window.bind("j", p1_move_W)
window.bind("k", p1_move_C)
window.bind("l", p1_move_E)
window.bind("n", p1_move_SW)
window.bind("m", p1_move_S)
window.bind(",", p1_move_SE)

#if p1_move_NW,p1_move_W,p1_move_SW

#if moves>1

#import turtle
#from turtle import *

p2moves=0

def p2_move_NW (self):
    global p1_y
    global currentgo
    global NW
    if currentgo  == 'player1' and NW == False:
        print ('error: It is the turn of player1')
        NW = True
    else:
        canvas.create_oval(70,70, 130, 130)
        currentgo = 'player1'
    

def p2_move_N(Self):
    global p1_y
    global currentgo
    global N
    if currentgo  == 'player1' and N == False:
        print ('error: It is the turn of player1')
        N = True
    else:
        canvas.create_oval(170,70,230,130)
        currentgo = 'player1'
        

def p2_move_NE(self):
    global p1_y
    global currentgo
    global NE
    if currentgo  == 'player1' and NE == False:
        print ('error: It is the turn of player1')
        NE = True
    else:
        canvas.create_oval(270,70,330,130)
        currentgo = 'player1'
    

def p2_move_W(self):
    global p1_y
    global currentgo
    global W
    if currentgo  == 'player1' and W == False:
        print ('error: It is the turn of player1')
        W = True
    else:
        canvas.create_oval(70,170, 130, 230)
        currentgo = 'player1'


def p2_move_SW(self):
    global p1_y
    global currentgo
    global SW
    if currentgo  == 'player1' and SW == False:
        print ('error: It is the turn of player1')
        SW = True
    else:
        canvas.create_oval(70,270,130,330)
        currentgo = 'player1'


def p2_move_S(self):
    global p1_y
    global currentgo
    global S
    if currentgo  == 'player1' and S == False:
        print ('error: It is the turn of player1')
        S = True
    else:
        canvas.create_oval(170,270,230,330)
        currentgo = 'player1'


def p2_move_SE(self):
    global p1_y
    global currentgo
    global SE
    if currentgo  == 'player1' and SE == False:
        print ('error: It is the turn of player1')
        SE = True
    else:
        canvas.create_oval(270,270,330,330)
        currentgo = 'player1'


def p2_move_E(self):
    global p1_y
    global currentgo
    global E
    if currentgo  == 'player1' and E == False:
        print ('error: It is the turn of player1')
        E =  True
    else:
        canvas.create_oval(270,170,330,230)
        currentgo = 'player1'



def p2_move_C(self):
    global p1_y
    global currentgo
    global C
    if currentgo  == 'player1' and C == False:
        print ('error: It is the turn of player1')
        C = True
    else:
        canvas.create_oval(170,170,230,230)
        currentgo = 'player1'
    

window.bind("q", p2_move_NW)
window.bind("w", p2_move_N)
window.bind("e", p2_move_NE)
window.bind("a", p2_move_W)
window.bind("s", p2_move_C)
window.bind("d", p2_move_E)
window.bind("z", p2_move_SW)
window.bind("x", p2_move_S)
window.bind("c", p2_move_SE)

#work out if you can bind one key for multiple commands




    

window.mainloop ()

