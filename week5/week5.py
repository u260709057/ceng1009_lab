# import random
# for i in range(10):
#     print(random.random())
import math
import turtle


# import random
# for i in range(10):
#     print(random.randint(25,35))

# import math
# hypotenuse = math.hypot(3,4)
# print(hypotenuse)

# a = int(input("Enter lenght: "))
# b = int(input("Enter width: "))
# hypotenuse = math.sqrt(a**2 + b**2)
# print(hypotenuse)

# import math
# def areaofcircle(radius):
#     area = math.pi * (radius**2)
#     return area
# print(areaofcircle(5))

# import turtle
# def drawstar(t, side ):
#  for i in range(5):
#      t.forward(side)
#      t.right(144)
# screen =turtle.Screen()
# tess = turtle.Turtle()
# drawstar(tess,100)
# screen.exitonclick()


def draw_square(t, side ):
    for i in range(4):
        t.forward(side)
        t.left(90)

# import turtle
# tess = turtle.Turtle()
# screen = turtle.Screen()
# screen.bgcolor("lightgreen")
# tess.color("pink")
# tess.pensize(3)
# for i in range(5):
#     draw_square(tess,20)
#     tess.penup()
#     tess.forward(40)
#     tess.pendown()


import turtle
screen = turtle.Screen()
tess = turtle.Turtle()
screen.bgcolor("lightgreen")
tess.color("red")
tess.pensize(3)

for i in range(20 , 120 , 10):
    draw_square(tess, i)
    tess.penup()
    tess.backward(5)
    tess.right(90)
    tess.forward(5)
    tess.left(90)
    tess.pendown()
screen.exitonclick()