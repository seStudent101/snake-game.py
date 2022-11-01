from turtle import *
from random import randrange
from freegames import square, vector
yemek = vector(0, 0)
yılan = [vector(10, 0)]
aim = vector(0, -10)
def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y
def inside(kafa):
    "Return True if head inside boundaries."
    return -200 < kafa.x < 190 and -200 < kafa.y < 190
def move():
    "Move snake forward one segment."
    kafa = yılan[-1].copy()
    kafa.move(aim)
    if not inside(kafa) or kafa in yılan:
        square(kafa.x, kafa.y, 9, 'red')
        update()
        return
    yılan.append(kafa)
    if kafa == yemek:
        print('Snake:', len(yılan))
        yemek.x = randrange(-15, 15) * 10
        yemek.y = randrange(-15, 15) * 10
    else:
        yılan.pop(0)
    clear()
    for vücut in yılan:
        square(vücut.x, vücut.y, 9, 'black')
    square(yemek.x, yemek.y, 9, 'green')
    update()
    ontimer(move, 100)
setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()