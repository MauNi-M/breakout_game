from turtle import *


class BreakOutBall(Turtle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # boundries
        self.upper_boundary = 280
        self.right_boundary = 380
        self.left_boundary = -380
        self.lower_boundary = -230

        # initial position
        self.body_x_pos = 0
        self.body_y_pos = -230

        # move step
        self.x_move = 1
        self.y_move = 1

        # turtle object
        self.penup()
        self.color("white", "white")
        self.shape("circle")
        self.setposition(self.body_x_pos, self.body_y_pos)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.setposition(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

