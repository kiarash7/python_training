import turtle

t = turtle.Turtle()

def square():
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
def two_square():
    square()
    t.forward(100)
    square()

elephant_weight = 3000
ant_weight = 0.01

if  elephant_weight > ant_weight:
    square()
else:
    two_square()


