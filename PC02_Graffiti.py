#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lilly McNichols and Caroline Holzapfel
September 7, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)


#=======Add your code here======
t=turtle.Turtle()
turtle.color("red1")
turtle.pensize(10)
turtle.circle(100)
turtle.up()
turtle.goto(-37,15)
turtle.down()
turtle.left(60)
turtle.forward(192)
turtle.up()
turtle.goto(180,-90)
turtle.color("tan3")
turtle.fillcolor()
turtle.rt(60)
turtle.begin_fill()
turtle.forward(180)
turtle.rt(90)
turtle.forward(130)
turtle.rt(90)
turtle.forward(180)
turtle.rt(90)
turtle.forward(130)
turtle.end_fill()
turtle.color("DodgerBlue1")
turtle.goto(185,-135)
turtle.down()
turtle.pensize(3)
turtle.circle(-80,-180)
turtle.right(60)
turtle.forward(20)
turtle.up()
turtle.backward(20)
turtle.down()
turtle.left(90)
turtle.forward(20)
turtle.up()
turtle.color("black")
turtle.goto(-200,300)
turtle.write("CANCEL JEFF",font = ("Verdana",50,"normal"))
#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
#turtle.done()
