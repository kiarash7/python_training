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

kia = 'Happy'

while kia == 'Happy':
    square()
    kia = 'Sad'
