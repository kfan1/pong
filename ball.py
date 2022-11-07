import random
from turtle import Turtle
from screen import *
from paddles import *
SHAPE = 'circle'
COLOR = 'blue'



class Ball:
    def __init__(self):
        self.ball = Turtle()
        self.ball.penup()
        self.ball.shape(SHAPE)
        self.ball.color(COLOR)
        self.ball_movement()
        self.heading = random.choice([random.randint(15, 45), random.randint(-45, -15)])
        self.ball.seth(self.heading)

    def ball_movement(self):
        self.ball.fd(3)

    def bouncing_off_walls(self):
        if self.ball.ycor() > HEIGHT/2 or self.ball.ycor() < -HEIGHT/2:
            self.heading *= -1
            self.ball.seth(self.heading)

    def scoring(self):
        if self.ball.xcor() > WIDTH/2:
            return 1
        elif self.ball.xcor() < -WIDTH/2:
            return 2
        else:
            return 0


    def bouncing_off_paddles(self, paddle):
        for _ in range(LENGTH):
            if self.ball.distance(paddle[_]) < 20 and -WIDTH / 2 + 50 < self.ball.xcor() < WIDTH / 2 - 50:
                self.heading = -self.heading + 180
                self.ball.seth(self.heading)