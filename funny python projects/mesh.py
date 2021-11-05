import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("Black")
t.pencolor("yellow")
t.speed(0)

for i in range(180):
    t.circle(900-i,90)
    t.lt(60)
    t.circle(900-i,90)
    t.lt(18)
