#!/usr/bin/env python
# coding=utf-8
import turtle
turtle.setup(650,650,300,300)
turtle.penup()
turtle.fd(-100)
turtle.pendown()
turtle.pensize(5)
for i in range(18):
        turtle.pencolor("purple")
        turtle.fd(-20)
        turtle.right(90)
        turtle.pencolor("pink")
        turtle.circle(-10,340)
        turtle.left(60)
        turtle.pencolor("purple")
        turtle.fd(22)
        turtle.left(90)
        turtle.pencolor("green")
        turtle.circle(-250,10)
        turtle.right(90)
turtle.done()
