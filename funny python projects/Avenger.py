import turtle

av = turtle.Turtle()
s = turtle.Screen()

s.bgcolor("black")
av.speed(10)
av.penup()
av.pensize(10)
# outer circle
av.setposition(0, -280)
av.pendown()
av.begin_fill()
av.color("red")
av.circle(300)
av.end_fill()
av.penup()

# inner circle
av.pensize(2)
av.setposition(0, -230)
av.pendown()
av.begin_fill()
av.color("black")
av.circle(250)
av.end_fill()
av.penup()

# drawing 'A'
av.setposition(30, -110)
av.pendown()
av.begin_fill()
av.color("red")
av.pensize(10)
av.pencolor("black")
av.forward(23)
av.backward(123)
av.left(60)
av.backward(220)
av.right(60)
av.backward(100)
av.right(117)
av.backward(710)
av.right(63)
av.backward(110)
av.right(90)
av.backward(510)
av.right(90)
av.backward(100)
av.right(90)
av.backward(70)
av.end_fill()
av.penup()

# Triangle shape in 'A' to make it look like 2d
av.pensize(10)
av.setposition(53, -40)
av.pendown()
av.begin_fill()
av.color("black")
av.pencolor("black")
av.right(90)
av.forward(100)
av.right(115)
av.forward(250)
av.right(157)
av.forward(227)
av.end_fill()

# arrow
av.backward(80)
av.left(42)
av.forward(147)
av.right(83)
av.forward(160)

turtle.done()