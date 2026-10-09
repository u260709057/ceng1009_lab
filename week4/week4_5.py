import turtle

screen = turtle.Screen()
screen.bgcolor("lightgreen")


t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
t.pensize(3)
t.stamp()
t.penup()
for i in range(12):
    t.forward(100)
    t.pendown()
    t.forward(20)
    t.penup()
    t.forward(20)
    t.stamp()
    t.backward(140)
    t.right(30)


screen.exitonclick()