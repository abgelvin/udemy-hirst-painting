from turtle import Turtle, Screen
import random

# import colorgram
# from PIL import Image

# image = Image.open('image.jpg')
# colors = colorgram.extract(image, 30)
# color_list = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_list.append((r, g, b))
# print(color_list)

my_turtle = Turtle()
screen = Screen()
screen.colormode(255)

my_turtle.shape('turtle')
my_turtle.color('green')
my_turtle.speed(0)
my_turtle.hideturtle()

rgb_colors = [(235, 234, 232), (235, 232, 234), (184, 148, 94), (152, 104, 46), (178, 150, 22), (83, 34, 27), (228, 229, 231), (12, 57, 73), (31, 100, 120), (101, 41, 48), (57, 137, 121), (108, 40, 29), (22, 65, 50), (40, 80, 7), (94, 62, 68), (110, 8, 9), (199, 91, 65), (116, 167, 77), (131, 178, 92), (224, 231, 225), (139, 167, 175), (216, 202, 142), (178, 147, 150), (179, 205, 177), (225, 177, 167), (157, 110, 113), (27, 75, 93), (97, 141, 148), (214, 178, 181), (168, 202, 208)]


def draw_row(x, y):
     for _ in range(10):
        my_turtle.penup()
        my_turtle.goto(x, y)
        x += 50
        my_turtle.dot(20, random.choice(rgb_colors))


def draw_box(x, y):
    for _ in range(10):
        draw_row(x, y)
        y += 50


draw_box(-200,-200)




screen.exitonclick()
