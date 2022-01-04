import random

from paddle import Paddle
from bricks import BrickBoard
from scoreboard import ScoreBoard
from ball import BreakOutBall
from turtle import *


skew = 2
# screen parameters
screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
canvas = screen.getcanvas()
canvas.config(borderwidth=0, highlightthickness=0)
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

brick_index = 0


def brick_breaking():
    number_of_bricks = len(game_board.bricks) - 1
    if game_ball.ycor() > -150:
        for index in range(number_of_bricks):
            if game_board.bricks[index].distance(game_ball) < 10:
                print("touched")
                game_board.bricks[index].hideturtle()
                del game_board.bricks[index]


# Ball Movement
def move_ball():
    # detect left or right wall
    if ball_collision_with(boundary=((-400, -300), (-400, 300)), orientation=True, rt_lb=False) or ball_collision_with(boundary=((400, -300), (400, 300)), orientation=True, rt_lb=True):
        game_ball.bounce_x()

    # detect ceiling collision
    if ball_collision_with(boundary=((-400, 300), (400, 300)), orientation=False, rt_lb=True):
        game_ball.bounce_y()

    # detect paddle collision
    if ball_collision_with(boundary=game_paddle.current_boundaries(), orientation=False, rt_lb=False):
        game_ball.bounce_y()
        game_ball.sety(game_ball.ycor())

    # detect brick collision
    number_of_bricks = len(game_board.bricks)
    for index in range(number_of_bricks):
        brick = game_board.bricks[index]
        collision = False
        if brick == 0:
            continue
        if ball_collision_with(*brick.upper_border):
            game_ball.sety(game_ball.ycor()+random.randint(0, skew))
            game_ball.bounce_y()
            collision = True
        if ball_collision_with(*brick.lower_border):
            game_ball.sety(game_ball.ycor()-random.randint(0, skew))
            game_ball.bounce_y()
            collision = True
        if ball_collision_with(*brick.left_border):
            game_ball.setx(game_ball.xcor() + random.randint(0, skew))
            game_ball.bounce_x()
            collision = True
        if ball_collision_with(*brick.right_border):
            game_ball.setx(game_ball.xcor() - random.randint(0, skew))
            game_ball.bounce_x()
            collision = True
        if collision:
            brick.hideturtle()
            game_board.bricks[index] = 0

    game_ball.move()
    canvas.after(ms=10, func=move_ball)


# Mouse Movement
def get_mouse_x():
    x_coor = canvas.winfo_pointerx() - 694
    game_paddle.move_paddle(x_coor)
    screen.update()
    canvas.after(ms=20, func=get_mouse_x)


def ball_collision_with(boundary: tuple, orientation: bool, rt_lb: bool) -> bool:
    """

    :param boundary: tuple of tuples, with coordinates of boundaries, (L,R); (T,B), ((x1, y1), (x2, y2))
    :param orientation: True means Vertical False means Horizontal
    :param rt_lb: True means Right or Top, False means Left or Bottom, direction of the ball
    :return bool: True if ball collided with boundary
    """
    # boundary is vertical and depending on LT or RB you add or subtract ball radius. If boundary is on the left which
    # means LB_RT is False, the radius is added to the boundary, otherwise the radius is subtracted
    if orientation:
        x = boundary[0][0] + game_ball.radius * (-1) ** rt_lb
        y_max = boundary[1][1] - game_ball.radius
        y_min = boundary[0][1] + game_ball.radius
        # print(f"x: {x}, y_min:{y_min}, y_max: {y_max}")
        if game_ball.xcor() == x and y_min < game_ball.ycor() < y_max:
            return True
        else:
            return False
    else:
        y = boundary[0][1] + game_ball.radius * (-1) ** rt_lb
        x_max = boundary[1][0]
        x_min = boundary[0][0]
        if game_ball.ycor() == y and x_min < game_ball.xcor() < x_max:
            return True
        else:
            return False


get_mouse_x()
move_ball()
brick_breaking()
# screen running
screen.mainloop()
