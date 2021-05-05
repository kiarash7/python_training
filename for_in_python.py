import turtle

t = turtle.Turtle()
t.speed(2)

def angle():
    t.forward(100)
    t.right(135)
    t.forward(70)
    t.right(90)
    t.forward(70)
def angle2():
    t.forward(100)
    t.right(90)
    t.forward(70)
    t.right(135)
    t.forward(70)
for i in range(8):
    angle()

for i in range(8):
    angle2()
