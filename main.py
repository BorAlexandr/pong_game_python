
from turtle import Screen
from jacket_computer import Jacket
from pong_ball import PongBall
from score_table import ScoreTable
import time

RIGHT_COORDINATES = (350, 0)
LEFT_COORDINATES = (-350, 0)

screen = Screen()
screen.bgcolor("black")
screen.title("Pong game")
screen.setup(width=800, height=600)
screen.tracer(0)

score_table = ScoreTable()

right_jacket = Jacket(RIGHT_COORDINATES)
left_jacket = Jacket(LEFT_COORDINATES)

pong_ball = PongBall()

screen.listen()
screen.onkey(fun=right_jacket.move_up, key="Up")
screen.onkey(fun=right_jacket.move_down, key="Down")
screen.onkey(fun=left_jacket.move_up, key="w")
screen.onkey(fun=left_jacket.move_down, key="s")

game_is_on = True
speed = 0.1


while game_is_on:
    screen.update()
    time.sleep(speed)
    pong_ball.move_ball()

    #Detect collision with up wall
    if pong_ball.ycor() > 280 or pong_ball.ycor() < -280:
        pong_ball.bounce_y()

    #Detect collision with jacket
    if pong_ball.distance(right_jacket) < 50 and pong_ball.xcor() > 320 or pong_ball.distance(left_jacket) < 50 and pong_ball.xcor() < -320:
        pong_ball.bounce_x()
        speed -= 0.01


    #Detect collision with right wall
    if pong_ball.xcor() > 380:
        pong_ball.reset_position_ball()
        score_table.l_score += 1
        score_table.update_score()
        speed = 0.1

    # Detect collision with left wall
    if pong_ball.xcor() < -380:
        pong_ball.reset_position_ball()
        score_table.r_score += 1
        score_table.update_score()
        speed = 0.1



screen.exitonclick()
