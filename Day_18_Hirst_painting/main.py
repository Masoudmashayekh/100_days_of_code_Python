# import colorgram
from turtle import Turtle, Screen
import random
import turtle
#
# rgb_list = []
# colors = colorgram.extract("image.jpg", 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_list.append(new_color)
#
# print(rgb_list)
color_list = [(248, 245, 246), (213, 154, 96), (51, 107, 132), (202, 142, 31), (180, 77, 30), (115, 155, 171),
              (124, 79, 99), (122, 175, 156), (230, 236, 239), (226, 198, 131), (241, 247, 243), (192, 87, 108),
              (10, 50, 64),
              (55, 38, 18), (44, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160),
              (38, 32, 35), (2, 26, 25), (78, 148, 171), (169, 23, 18), (17, 79, 91), (236, 165, 169),
              (178, 204, 185), (49, 62, 84), (184, 190, 202), (166, 203, 207), (79, 68, 42), (11, 113, 110)]
turtle.colormode(255)
timmy = Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = Screen()
screen.exitonclick()
