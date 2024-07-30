from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(fun=l_paddle.up, key='w')
screen.onkeypress(fun=l_paddle.down, key='s')
screen.onkeypress(fun=r_paddle.up, key='Up')
screen.onkeypress(fun=r_paddle.down, key='Down')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()

    # ball.check_for_bounce()


screen.exitonclick()
