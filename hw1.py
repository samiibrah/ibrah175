# Your Name:#Samia Ibrahim

import turtle, platform

#TODO: Fill out the Purpose, Input Parameter(s), and Return Value
# for each of the two functions below in comments

#Remember, you must place a # before any comment, or it will be
# interpreted as Python code, and will probably cause errors.

#Part 1: cents
#==========================================
# Purpose: #computes the number of pennies, quarters, dimes and nickles specified. 
#   
# Input Parameter(s): # quarters, dimes, nickels, pennies
#   
# Return Value: #computes the total number of quarters, dimes, nickles, and pennies. 
#   
#==========================================
#def cents(1,0,-1,3)
#return 23
def cents(quarters, dimes, nickels, pennies):
    total = 0
    total += quarters*25
    total += dimes*10
    total += nickels*5
    total += pennies
    return total

#Part 2: draw_M
#==========================================
# Purpose: # draw the signature M logo for the University of Minnesota
#   
# Input Parameter(s): #turtle.color for the two colors used. Turtle.forward to move the turle, turtle
#  right to move the turtle right and turtle fill to color in the finished logo
#
# Return Value:#this code returns a gold and maroon picture of the M logo
#   
#==========================================
#def draw_M

def draw_M():
    turtle.delay(0)
    turtle.bgcolor("gold")
    turtle.hideturtle()
    turtle.color("maroon")
    turtle.penup()
    turtle.setpos(-200,-100)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(14)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(128)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(14)
    turtle.right(120)
    turtle.forward(28)
    turtle.right(120)
    turtle.forward(80)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(28)
    turtle.right(60)
    turtle.forward(140)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(52)
    turtle.right(120)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(120)
    turtle.left(90)
    turtle.forward(64)
    turtle.left(90)
    turtle.forward(20)
    turtle.right(120)
    turtle.forward(140)
    turtle.right(60)
    turtle.forward(28)
    turtle.left(90)
    turtle.forward(64)
    turtle.end_fill()

vers = platform.python_version()
assert vers[0] == '3', "You must use Python 3, "+vers+" is not acceptable"
