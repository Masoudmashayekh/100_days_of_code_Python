from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    scoreboard.center_line()
    screen.update()
    ball.move_ball()

    # Detect collision with wall:
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.bounce_y()

    # Detect collision with paddle:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect paddle misses:
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
screen.exitonclick()
