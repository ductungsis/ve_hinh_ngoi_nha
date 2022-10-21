

import turtle
import math

# background color
screen = turtle.Screen()
screen.bgcolor("skyblue")

# Create turtle
turtle = turtle.Turtle()
turtle.color("black")
turtle.shape("turtle")
turtle.speed(10)

# hinh tam giac
def drawRectangle(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.forward(width)
  t.left(90)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# mai nha
def drawTriangle(t, length, color):
  t.fillcolor(color)
  t.begin_fill()
  t.forward(length)
  t.left(135)
  t.forward(length / math.sqrt(2))
  t.left(90)
  t.forward(length / math.sqrt(2))
  t.left(135)
  t.end_fill()
  
# canh nha
def drawParallelogram(t, width, height, color):
  t.fillcolor(color)
  t.begin_fill()
  t.left(30)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(120)
  t.forward(width)
  t.left(60)
  t.forward(height)
  t.left(90)
  t.end_fill()
  
# mat troi va tia nang mat troi
def drawFourRays(t, length, radius):
  for i in range(4):
    t.penup()
    t.forward(radius)
    t.pendown()
    t.forward(length)
    t.penup()
    t.backward(length + radius)
    t.left(90)

# mat truoc cua nha
turtle.penup() 
turtle.goto(-150, -120)
turtle.pendown()
drawRectangle(turtle, 100, 110, "blue")

# cua
turtle.penup()
turtle.goto(-120, -120)
turtle.pendown()
drawRectangle(turtle, 40, 60, "lightgreen")

# mai nha
turtle.penup()
turtle.goto(-150, -10)
turtle.pendown()
drawTriangle(turtle, 100, "magenta")

# canh nha
turtle.penup()
turtle.goto(-50, -120)
turtle.pendown()
drawParallelogram(turtle, 60, 110, "yellow")

# cua so
turtle.penup()
turtle.goto(-30, -60)
turtle.pendown()
drawParallelogram(turtle, 20, 30, "brown")

# canh mai nha
turtle.penup()
turtle.goto(-50, -10)
turtle.pendown()
turtle.fillcolor("orange")
turtle.begin_fill()
turtle.left(30)
turtle.forward(60)
turtle.left(105)
turtle.forward(100 / math.sqrt(2))
turtle.left(75)
turtle.forward(60)
turtle.left(105)
turtle.forward(100 / math.sqrt(2))
turtle.left(45)
turtle.end_fill()

# goc cay
turtle.penup() 
turtle.goto(100, -130)
turtle.pendown()
drawRectangle(turtle, 20, 40, "brown")

# ngon cay
turtle.penup() 
turtle.goto(65, -90)
turtle.pendown()
drawTriangle(turtle, 90, "lightgreen")
turtle.penup() 
turtle.goto(70, -45)
turtle.pendown()
drawTriangle(turtle, 80, "lightgreen")
turtle.penup() 
turtle.goto(75, -5)
turtle.pendown()
drawTriangle(turtle, 70, "lightgreen")

# Sun
turtle.penup() 
turtle.goto(55, 110)
turtle.fillcolor("yellow")
turtle.pendown()
turtle.begin_fill()
turtle.circle(24)
turtle.end_fill()

# tia nang
turtle.penup()
turtle.goto(55, 134)
turtle.pendown()
drawFourRays(turtle, 25, 24)
turtle.right(45)
drawFourRays(turtle, 15, 24)
turtle.left(45)

#labels
turtle.color("black")
turtle.penup()
turtle.goto(-150, 70)
turtle.pendown()
turtle.write("House", None, None, "14pt bold")
turtle.penup()
turtle.goto(150, -150)
turtle.pendown()
turtle.write("Tree", None, None, "14pt bold")
turtle.penup()
turtle.goto(130, 150)
turtle.pendown()
turtle.write("Sun", None, None, "14pt bold")

# bring turtle back
turtle.penup()
turtle.goto(-100, -150)
turtle.left(90)

