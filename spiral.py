#!/usr/bin/env python
# coding=utf-8
import turtle
import time

turtle.speed("fastest")
turtle.pensize(2)
for x in range(100):
    turtle.forward(2 * x)  # 每次画的长度是变量x的2倍
    turtle.left(90)  # 逆时针旋转90°

time.sleep(3)
