from turtle import Turtle, Screen
import random


my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

my_turtle.shape('turtle')
my_turtle.color('green')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


def draw_dashed_line():
    for _ in range(15):
        my_turtle.forward(10)
        my_turtle.penup()
        my_turtle.forward(10)
        my_turtle.pendown()


def draw_shapes():
    my_turtle.speed(10)
    sides = 3
    
    while sides < 11:
        angle = 360 / sides
        my_turtle.pencolor(random_color())
        for i in range(sides):
            my_turtle.forward(100)
            my_turtle.left(angle)
        sides += 1
        

def draw_random_walk():
    my_turtle.pensize(10)
    my_turtle.speed(0)
    
    for _ in range(200):
        direction = random.choice([0, 90, 180, 270])
        my_turtle.setheading(direction)
        my_turtle.pencolor(random_color())
        my_turtle.forward(30)
      

def draw_spirograph():
    my_turtle.speed(0)
    heading = 0
    
    while heading < 360:
        my_turtle.setheading(heading)
        my_turtle.pencolor(random_color())
        my_turtle.circle(100)
        heading += 5






# draw_square()
# draw_dashed_line()
# draw_shapes()
# draw_random_walk()
draw_spirograph()


screen.exitonclick()


