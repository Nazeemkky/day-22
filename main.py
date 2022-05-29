import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

ball01 = Ball()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=paddle.top)
screen.onkey(key="Down", fun=paddle.down)
screen.onkey(key="w", fun=paddle_left.top)
screen.onkey(key="s", fun=paddle_left.down)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball01.move_speed)

    ball01.move()

    if ball01.ycor() > 280 or ball01.ycor() < -280:
        ball01.bounce_y()

        # find the ball is missing the paddle or not
    if ball01.distance(paddle) < 50 \
            and ball01.xcor() > 340 \
            or ball01.distance(paddle_left) < 50 \
            and ball01.xcor() < -340:
        ball01.bounce_x()

    # checking the right part missing or not and  restarting
    if ball01.xcor() > 380:
        ball01.reset_position()
        score.increase_left()

    # checking the left part missing or not and  restarting
    if ball01.xcor() < -380:
        ball01.reset_position()
        score.increase_l()

screen.exitonclick()
