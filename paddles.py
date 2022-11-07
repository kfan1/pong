from turtle import Turtle
from screen import *

LENGTH = 5
PDCOLOR = 'white'
PDSHAPE = 'square'


class Paddle:
    def __init__(self):
        self.paddle1 = []
        self.paddle2 = []
        self.creation1()
        self.creation2()

    def creation1(self):
        for _ in range(LENGTH):
            self.paddle1.append(Turtle())
            self.paddle1[_].penup()
            self.paddle1[_].color(PDCOLOR)
            self.paddle1[_].shape(PDSHAPE)
            self.paddle1[_].goto(x=-WIDTH/2+50, y=(((1-LENGTH)/2+_)*20))

    def creation2(self):
        for _ in range(LENGTH):
            self.paddle2.append(Turtle())
            self.paddle2[_].penup()
            self.paddle2[_].color(PDCOLOR)
            self.paddle2[_].shape(PDSHAPE)
            self.paddle2[_].goto(x=WIDTH/2-50, y=(((1-LENGTH)/2+_)*20))

    def movementup(self):
        for element in self.paddle1:
            element.seth(90)
            element.fd(10)

    def movementdown(self):
        for element in self.paddle1:
            element.seth(270)
            element.fd(10)

    def computer_movement(self, ball):
        if ball.xcor() < 0:
            return
        if ball.ycor() > self.paddle2[2].ycor():
            for element in self.paddle2:
                element.seth(90)
                element.fd(2)

        if ball.ycor() < self.paddle2[2].ycor():
            for element in self.paddle2:
                element.seth(270)
                element.fd(2)
