import turtle
import random
# setup the window with a background colour
window = turtle.Screen()

# assign a name to your turtle
t = turtle.Turtle()
t.speed(0)

# create one branch of the snowflake
def branch():
    for i in range(3):
        for i in range(3):
            t.forward(30)
            t.backward(30)
            t.right(45)
        t.left(90)
        t.backward(30)
        t.left(45)
    t.right(90) 
    t.forward(90)

for i in range(8):
    branch()
    t.left(45)
