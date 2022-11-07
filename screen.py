from turtle import Turtle, Screen
WIDTH = 900
HEIGHT = 600
BGCOLOR = 'black'
TITLE = 'Pong'


class ScreenCreate:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=WIDTH, height=HEIGHT)
        self.screen.bgcolor(BGCOLOR)
        self.screen.title(TITLE)
        self.writing_turtle1 = Turtle()
        self.score_keeping_turtle1 = Turtle()

    def writing_turtle(self):
        self.writing_turtle1.speed(0)
        self.writing_turtle1.ht()
        self.writing_turtle1.color('white')
        self.writing_turtle1.penup()
        self.writing_turtle1.goto(x=0, y=HEIGHT/2-10)
        self.writing_turtle1.seth(270)
        for _ in range(int(HEIGHT/40)):
            self.writing_turtle1.pendown()
            self.writing_turtle1.fd(20)
            self.writing_turtle1.penup()
            self.writing_turtle1.fd(20)

    def score_keeping_turtle(self, user, opponent):
        self.score_keeping_turtle1.speed(0)
        self.score_keeping_turtle1.ht()
        self.score_keeping_turtle1.color('white')
        self.score_keeping_turtle1.penup()
        self.score_keeping_turtle1.goto(x=-WIDTH/3.5, y=HEIGHT/2-40)
        self.score_keeping_turtle1.pendown()
        self.score_keeping_turtle1.write(f'You {user}', align='center', font=('Comic Sans MS', 14, 'normal'))
        self.score_keeping_turtle1.penup()
        self.score_keeping_turtle1.goto(x=WIDTH/3.5, y=HEIGHT/2-40)
        self.score_keeping_turtle1.pendown()
        self.score_keeping_turtle1.write(f'Computer {opponent}', align='center', font=('Comic Sans MS', 14, 'normal'))

    def cont(self):
        cont = self.screen.textinput('Continue?', 'yes or no')
        if cont == 'yes':
            return True
        else:
            return False

    def final_turtle(self, user, opponent):
        final_turtle = Turtle()
        final_turtle.speed(0)
        final_turtle.ht()
        final_turtle.color('white')
        if user < opponent:
            final_turtle.write(f'You lose.\nYour score: {user}\nComputer score: {opponent}', align='center', font=('Comic Sans MS', 36, 'normal'))
        elif opponent < user:
            final_turtle.write(f'You win!\nYour score: {user}\nComputer score: {opponent}', align='center', font=('Comic Sans MS', 36, 'normal'))
        else:
            final_turtle.write(f'It\'s a draw.\nYour score: {user}\nComputer score: {opponent}', align='center', font=('Comic Sans MS', 36, 'normal'))





