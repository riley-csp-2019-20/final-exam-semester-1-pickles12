#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Tai Crabtree   
#Date
#12/19/20


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries

import turtle as trtl

#create turtle

drawer = trtl.Turtle()
pensize = 1
penup = 1

#movement functions

def up():
    drawer.forward(5)
def down():
    drawer.forward(-5)
def left():
    drawer.left(90)
def right(): 
    drawer.right(90)


#color/drawing functions

def Big():
    global pensize
    pensize += 1
    drawer.pensize(pensize)
def Small():
    global pensize
    if pensize > 0:
        pensize += -1
        drawer.pensize(pensize)
def pen():
    global penup
    
    if penup > 1:
        drawer.pendown()
        penup -= 1
    else:
        drawer.penup()
        penup += 1
def clear():
    drawer.clear()
#create screen

wn = trtl.Screen()

#bind to keypresses

wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(left,"Left")
wn.onkeypress(right,"Right")
wn.onkeypress(Big, "o")
wn.onkeypress(Small, "p")
wn.onkeypress(pen,"u")
wn.onkeypress(clear,"space")

#listen

wn.listen()

#mainloop

wn.mainloop()