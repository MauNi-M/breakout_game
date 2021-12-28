from paddle import Paddle
from bricks import BrickBoard
from scoreboard import ScoreBoard
from ball import BreakOutBall
from turtle import *

# screen parameters
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
canvas = screen.getcanvas()
current_screen_w, current_screen_h = canvas.winfo_screenwidth(), canvas.winfo_screenheight()
posx = current_screen_w // 2 - 400
posy = current_screen_h // 2 - 300
screen.setup(height=600, width=800, startx=posx, starty=posy)
screen.title("MauNi's Breakout")

# game objects
game_paddle = Paddle()
game_scoreboard = ScoreBoard()
game_board = BrickBoard()
game_ball = BreakOutBall()


def move_ball():
    # detect x axis collision
    if game_ball.xcor() < game_ball.left_boundary:
        game_ball.bounce_x()
        game_ball.setx(game_ball.xcor() + 2)
    if game_ball.xcor() > game_ball.right_boundary:
        game_ball.bounce_x()
        game_ball.setx(game_ball.xcor() - 2)
    # detect y_upper collision
    if game_ball.ycor() > game_ball.upper_boundary:
        game_ball.bounce_y()
        game_ball.sety(game_ball.ycor() - 2)

    # detect paddle collision
    if game_ball.ycor() == game_paddle.paddle_boundary:

        if game_ball.distance(game_paddle) <= game_paddle.paddle_width + 10:
            game_ball.bounce_y()
            game_ball.sety(game_ball.ycor() + 2)

    # detect brick collision


    game_ball.move()
    canvas.after(ms=1, func=move_ball)

def detect_proximity(brick):

    game_ball.distance(brick)
canvas.after(ms=1, func=move_ball)


# paddle movement

def get_mouse_x():
    x_coor = canvas.winfo_pointerx() - 694
    # print(f"mouse X position: {canvas.winfo_pointerx()}, corrected: {x_coor}")
    game_paddle.move_paddle(x_coor)
    screen.update()
    canvas.after(ms=17, func=get_mouse_x)


canvas.after(ms=17, func=get_mouse_x)

screen.mainloop()
