from time import *
from random import *
from turtle import *
from sys import *

# ::::::::::::::::::::::::::::::::::::::Variablen:::::::::::::::::::::::::::::::::::

winsizex = 1000
winsizey = 800
delay = 0.1
score = 0
segments = []

# ::::::::::::::::::::::::::::::::::::::WINDOW::::::::::::::::::::::::::::::::::::::

window = Screen()
window.title("snake")
window.bgcolor("black")
window.setup(width=winsizex, height=winsizey)
window.tracer(0)

# ::::::::::::::::::::::::::::::::::::head'dex:::::::::::::::::::::::::::::::::::::

snake_head = Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("green")
snake_head.shapesize(stretch_wid=1, stretch_len=1)
snake_head.goto(0, 0)
snake_head.penup()
snake_head.direction = "stop"

# ::::::::::::::::::::::::::::::::::::FOOD::::::::::::::::::::::::::::::::::::::::::
randx = randint(-winsizex//2, winsizex//2)
randy = randint(-winsizey//2, winsizey//2)

food = Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.shapesize(stretch_wid=1, stretch_len=1, outline=1)
food.penup()
food.goto(randx-20 , randy-20)

# :::::::::::::::::::::::::::::::::::::::MOVEMENT:::::::::::::::::::::::::::::::::::

def up():
    if snake_head.direction != "down":
        snake_head.direction = "up"

def down():
    if snake_head.direction != "up":
        snake_head.direction = "down"

def left():
    if snake_head.direction != "right":
        snake_head.direction = "left"

def right():
    if snake_head.direction != "left":
        snake_head.direction = "right"

def move():
    if snake_head.direction == "up":
        y = snake_head.ycor()
        snake_head.sety(y + 20)

    if snake_head.direction == "down":
        y = snake_head.ycor()
        snake_head.sety(y - 20)

    if snake_head.direction == "left":
        x = snake_head.xcor()
        snake_head.setx(x - 20)

    if snake_head.direction == "right":
        x = snake_head.xcor()
        snake_head.setx(x + 20)
 
window.listen()

window.onkeypress(up, "Up")
window.onkeypress(down,"Down")
window.onkeypress(right, "Right")
window.onkeypress(left,"Left")

# :::::::::::::::::::::::::::::::::::::::MAIN:::::::::::::::::::::::::::::::::::::::

while True:
    randx = randint(-winsizex//2, winsizex//2)
    randy = randint(-winsizey//2, winsizey//2)
    window.update()

    if snake_head.xcor()>winsizex//2 or snake_head.xcor()<-winsizex//2 or snake_head.ycor()>winsizey//2 or snake_head.ycor()<-winsizey//2:
        print("Deine Punktzahl ist:", score)
        exit()
    if snake_head.distance(food) < 20:
        food.goto(randx-20, randy-20)
        score += 1

        #::::::::::Segment::::::::::

        new_segment = Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.shapesize(stretch_wid=1, stretch_len=1)
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001


    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)

    if len(segments) > 0:
        x = snake_head.xcor()
        y = snake_head.ycor()
        segments[0].goto(x, y)

    move()

    #::::::::::Game Over::::::::::

    for new_segment in segments:
        if new_segment.distance(snake_head) < 20:
            print("Deine Punktzahl ist:", score)
            exit()
            

    sleep(delay)