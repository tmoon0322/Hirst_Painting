import turtle

import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r, g, b))
# print(rgb_colors)


from turtle import Turtle, Screen
import random

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157),
              (215, 74, 12), (15, 154, 16), (199, 14, 10), (243, 33, 165), (229, 17, 121), (73, 9, 31),
              (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232), (11, 227, 239),
              (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)]
turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()


def paint_table(row_count, row_length):
    y_value = -250
    timmy.goto(-300, y_value)
    for _ in range(row_count):
        for _ in range(row_length):
            timmy.color(random.choice(color_list))
            timmy.dot(25)
            timmy.forward(50)
        y_value += 50
        timmy.goto(-300, y_value)
    timmy.hideturtle()


paint_table(10, 10)


screen = Screen()
screen.exitonclick()
