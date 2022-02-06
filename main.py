import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
coloor = [
    (232, 251, 242), (198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46),
    (27, 40, 157), (215, 74, 12), (15, 154, 16), (199, 14, 10), (242, 246, 252), (243, 33, 165), (229, 17, 121),
    (73, 9, 31), (60, 14, 8), (224, 141, 211), (10, 97, 61), (221, 160, 9), (17, 18, 43), (46, 214, 232),
    (11, 227, 239), (81, 73, 214), (238, 156, 220), (74, 213, 167), (77, 234, 202), (52, 234, 243), (3, 67, 40)
]
# cl = coloor[random.randint(0, len(coloor)-1)]
# print(cl)
toshbaqa = Turtle()
screen = Screen()
toshbaqa.shape("circle")
# toshbaqa.speed(1)
toshbaqa.hideturtle()
toshbaqa.speed(speed=150)
x = -280
y = -220
for _ in range(10):
    toshbaqa.penup()
    toshbaqa.setx(x)
    toshbaqa.sety(y)
    for tosh in range(10):
        cl = coloor[random.randint(0, len(coloor)-1)]
        # toshbaqa.color(cl)
        toshbaqa.dot(30, cl)
        toshbaqa.penup()
        toshbaqa.forward(50)
        toshbaqa.pendown()
        toshbaqa.forward(0)

    y += 50

screen.exitonclick()
