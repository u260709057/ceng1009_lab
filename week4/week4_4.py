import turtle
t=turtle.Turtle()
screen=turtle.Screen()
t.penup()
t.goto(-200,0)
t.pendown()
for i in range(3):
    t.forward(80)
    t.left(120)
t.penup()
t.goto(-100,0)
t.pendown()
for i in range(4):
    t.forward(80)
    t.left(90)
t.penup()
t.goto(30,0)
t.pendown()
for i in range(6):
    t.forward(80)
    t.left(60)
t.penup()
t.goto(220,0)
t.pendown()
for i in range(8):
    t.forward(80)
    t.left(45)

screen.exitonclick()
