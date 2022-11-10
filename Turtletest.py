#Modules

import turtle
import sys
import os
import time
import random
import webbrowser

#Variables

colorn = 0
url =  "https://www.youtube.com/watch?v=lvwZQTB4iv4"
turtle.hideturtle()
n1 = 255
n2 = 0
n3 = 0

#Setup
turtle.colormode(255)
def changecolor():
    global n1
    global n2
    global n3
    colorchange = 1
    n1 = n1 + colorchange
    if n1 == 255:
        n2 = n2 + colorchange
    if n2 == 255:
        
        n1 = n1 - colorchange
#Start

#Triangle
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.clear()

#Pentagon
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.clear()

#Hexagon
for i in range(6):
    turtle.forward(100)
    turtle.left(60)
turtle.clear()

#Ten
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.forward(100)
turtle.left(36)
turtle.clear()

#Circle
turtle.circle(100)
turtle.clear()

#Star
for i in range(5):
 
        turtle.forward(100)
        turtle.right(144)
turtle.clear()

#Squares
count = 0
for i in range(3):
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    count = count - 100

    turtle.setpos(count,count)
webbrowser.open_new(url)