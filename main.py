from time import sleep

from paddle import Paddle
from bricks import BrickBoard
from scoreboard import ScoreBoard
from ball import BreakOutBall
from turtle import *

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
canvas = screen.getcanvas()

current_screen_w, current_screen_h = canvas.winfo_screenwidth(), canvas.winfo_screenheight()

posx = current_screen_w // 2 - 400
posy = current_screen_h // 2 - 300
screen.setup(height=600, width=800, startx=posx, starty=posy)
screen.title("MauNi's Breakout")

game_paddle = Paddle()
game_scoreboard = ScoreBoard()
game_board = BrickBoard()
game_ball = BreakOutBall()


def mouse_coor(event):
    screen.update()
    x_coor = event.x - 400
    game_paddle.move_paddle(x_coor)
    screen.update()

def move_ball():
    # detect x axis collision
    if game_ball.xcor() < game_ball.left_boundary:
        game_ball.bounce_x()
        game_ball.setx(game_ball.xcor()+5)
    if game_ball.xcor() > game_ball.right_boundary:
        game_ball.bounce_x()
        game_ball.setx(game_ball.xcor()-5)
    # detect y upper collision
    if game_ball.ycor() > game_ball.upper_boundary:
        game_ball.bounce_y()
        game_ball.sety(game_ball.ycor()-5)

    # detect paddle collision
    if game_ball.distance(game_paddle.body) < 20 or game_ball.distance(game_paddle):
        game_ball.bounce_y()

    game_ball.move()

    screen.update()
    canvas.after(ms=3, func=move_ball)

move_ball()
canvas.bind("<Motion>", mouse_coor)


screen.mainloop()
