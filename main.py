import time

from paddles import Paddle
from screen import ScreenCreate
from ball import Ball


screen = ScreenCreate()
screen.screen.tracer(n=0)
paddles = Paddle()
ball = Ball()
user = 0
computer = 0

screen.screen.onkeypress(paddles.movementup, key='Up')
screen.screen.onkeypress(paddles.movementdown, key='Down')


cont = True
while cont:
    screen.screen.listen()
    screen.score_keeping_turtle1.clear()
    ball.ball.goto(0, 0)
    screen.writing_turtle()
    screen.score_keeping_turtle(user, computer)
    game_on = True
    while game_on:
        screen.screen.update()
        time.sleep(0.01)
        ball.ball_movement()
        ball.bouncing_off_walls()
        ball.bouncing_off_paddles(paddles.paddle1)
        ball.bouncing_off_paddles(paddles.paddle2)
        paddles.computer_movement(ball.ball)
        score = ball.scoring()
        if score == 1:
            user += 1
            game_on = False
            cont = screen.cont()

        elif score == 2:
            computer += 1
            game_on = False
            cont = screen.cont()

    if not cont:
        screen.final_turtle(user, computer)




screen.screen.exitonclick()

