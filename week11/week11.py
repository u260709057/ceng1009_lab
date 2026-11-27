#
##EXAMPLE 1##
#
# def fizz_buzz(n):
#     for i in range(1, n+1):
#         if i % 3 == 0 and i % 5 == 0:
#             print('FizzBuzz')
#         elif i % 3 == 0:
#             print('Fizz')
#         elif i % 5 == 0:
#             print('Buzz')
#         else:
#             print(i)
# print(fizz_buzz(16))
#
###EXAMPLE 2##
#
# def digit_sum(n):
#     total = 0
#     while n > 0:
#         total += n % 10
#         n = n // 10
#     return total
# print(digit_sum(1234))
#
##EXAMPLE 3##
#
# def alternate_case(s):
#     result = ""
#     for i in range(len(s)):
#         if i % 2 == 0:
#             result = result + s[i].upper()
#         else:
#             result = result + s[i].lower()
#     return result
# print(alternate_case("hello world"))
#
##EXAMPLE 4##
#
# import turtle
# def draw_polygon(t,sides,lenght):
#     for i in range(sides):
#         t.forward(lenght)
#         t.left(360/sides)
# wn = turtle.Screen()
# wn.bgcolor("lightgreen")
# t = turtle.Turtle()
# t.pensize(3)
# color = ["red","black","blue"]
#
# for i in range(3):
#     t.penup()
#     t.goto(-150+i*120,0)
#     t.pendown()
#     t.color(color[i])
#     draw_polygon(t,i+3,60)
# wn.exitonclick()
#
##EXAMPLE 5:##
#
# import turtle
# def draw_square(t,lenght,color):
#  t.fillcolor(color)
#  t.begin_fill()
#  for i in range(4):
#      t.forward(lenght)
#      t.left(90)
#  t.end_fill()
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# wn.bgcolor("lightgreen")
# for i in range(5):
#     t.penup()
#     t.goto(-165 + i*70,-25)
#     t.pendown()
#     if i %2 == 0:
#         draw_square(t,50,"red")
#     else:
#         draw_square(t,50,"blue")
# wn.exitonclick()
#
##EXAMPLE 6 ##
#
#import turtle
# def drawsquare(t,lenght):
#     for i in range(4):
#         t.forward(lenght)
#         t.left(90)
# wn = turtle.Screen()
# wn.bgcolor("white")
# t = turtle.Turtle()
# t.pensize(2)
# for i in range(12):
#     drawsquare(t,80)
#     t.left(30)
# wn.exitonclick()
#
##EXAMPLE 7##
#
import turtle
from operator import length_hint


def drawsquare(t,lenght, filled):
    if filled:
        t.begin_fill()
    for i in range(4):
        t.forward(lenght)
        t.left(90)
    if filled:
        t.end_fill()

wn = turtle.Screen()
wn.bgcolor("white")
t = turtle.Turtle()
length = 40
for row in range(8):
    for col in range(8):
        t.penup()
        t.goto(-120 + col * length ,-120 + row * length)
        t.pendown()
        drawsquare(t, length, (row+col)% 2 == 0)
wn.exitonclick()

