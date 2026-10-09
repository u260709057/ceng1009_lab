import turtle
pirate = turtle.Turtle()
screen = turtle.Screen()

Angles = [160, -43, 270, -97, -43, 200, -940, 17, -86]
for angle in Angles:
    pirate.left(angle)
    pirate.forward(100)

print(f"Korsanın son yönü:", pirate.heading())

