# def sumTo(n):
#     return (n * (n + 1)) // 2
#
#
# print(sumTo(10))   # 55
# n = int(input("PLEASE ENTER A NUMBER"))
# print("Sum is", sumTo(n))

# import turtle
#
# def star(t, n, size):
#     for i in range(n):
#         t.forward(size)
#         t.right(180 - 180 / n)
#
# tess = turtle.Turtle()
# star(tess, 41, 100)
# screen = turtle.Screen()
# screen.exitonclick()
#
# def sumTo(n):
#     total = 0
#     for i in range(1, n + 1):
#         total += i
#     return total
# n = int(input("Enter a number: "))
# print(sumTo(n))  # 55


# def mySqrt(n):
#     guess = n / 2
#     for i in range(10):
#         guess = (1 / 2) * (guess + (n / guess))
#     return guess
# n = int(input("Enter A Number: "))
# m = int(input("Enter second Number: "))
# print(mySqrt(n))
# print(mySqrt(m))
#
# import turtle
#
# def drawSprite(someturtle, legs, lenght):
#     angle = 360 / legs
#     for i in range(legs):
#         someturtle.forward(lenght)
#         someturtle.backward(lenght)
#         someturtle.left(angle)
#
# def fancySquare(t,size):
#     for i in range(4):
#         drawSprite(t,8,20)
#         t.forward(size)
#         t.left(90)
#
# wn = turtle.Screen()
# t = turtle.Turtle()
# t.color("pink")
# t.pensize(2)
#
# fancySquare(t,100)
# wn.exitonclick()



# a = int(input("BİR SAYI GİRİNİZ."))
#
# if a < 0:
#  print("negatif")
# if a > 0:
#         print("positif")
# if a == 0:
#         print("zero")





import turtle

def barChart(data):
    t = turtle.Turtle()
    t.fillcolor("red")
    wn = turtle.Screen()
    wn.bgcolor("lightgreen")
    for h in data:
        t.begin_fill()
        t.left(90)
        t.forward(h)
        t.penup()
        t.left(90)
        t.write(h)
        t.right(90)
        t.pendown()
        t.right(90)
        t.forward(40)
        t.right(90)
        t.forward(h)
        t.left(90)
        t.end_fill()

barChart([48, 117, 200, 240, 160, 260, 220])
turtle.mainloop()
