#
# Drawing COVID19 shaped virus using Turtle Library
#
import turtle
trt = turtle.Turtle()
scr = turtle.Screen()
scr.bgcolor('black')
trt.pencolor('red')
a = 0
b = 0
trt.speed(0)
trt.penup()
trt.goto(0, 200)
trt.pendown()
while True:
    trt.forward(a)
    trt.right(b)
    a += 3
    b += 1
    if b == 210:
        break
    trt.hideturtle
turtle.done()
