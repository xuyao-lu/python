#!/usr/bin/env python
# coding=utf-8
import turtle

turtle.pensize(1)
turtle.bgcolor("black")
colors = ["pink"] * 4
#turtle.tracer(False)  # 跳过绘画过程
for x in range(200):
    turtle.forward(2 * x)
    turtle.color(colors[x % 4])
    turtle.left(91)
#turtle.tracer(True)
turtle.done()
