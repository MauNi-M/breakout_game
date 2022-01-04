from turtle import *


class Paddle(Turtle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.paddle_width = 80
        self.body_xpos = 0
        self.body_ypos = -250
        self.paddle_shape_maker()
        # body
        self.shape("myshape")

        self.color("white", "white")
        self.penup()
        self.setposition(x=self.body_xpos, y=self.body_ypos)

    def current_boundaries(self):
        return ((self.xcor()-self.paddle_width-5, self.body_ypos+10), (self.xcor()+self.paddle_width+5, self.body_ypos+10))

    def move_paddle(self, x_pos):
        if -320 < x_pos < 320:
            self.body_xpos = x_pos
            self.setx(self.body_xpos)

    def paddle_shape_maker(self):
        s = Shape("compound")
        right_half_circle = (
            (10, 0),
            (9.51, 3.09),
            (8.09, 5.88),
            (5.88, 8.09),
            (3.09, 9.51),
            (0, 10),
            (-3.09, 9.51),
            (-5.88, 8.09),
            (-8.09, 5.88),
            (-9.51, 3.09),
            (-10, 0))
        left_half_circle = (
            (10, 0),
            (-10, 0),
            (-9.51, -3.09),
            (-8.09, -5.88),
            (-5.88, -8.09),
            (-3.09, -9.51),
            (-0.0, -10.0),
            (3.09, -9.51),
            (5.88, -8.09),
            (8.09, -5.88),
            (9.51, -3.09)
        )
        middle_part = (
            (10.0, -float(self.paddle_width)),
            (10.0, float(self.paddle_width)),
            (-10.0, float(self.paddle_width)),
            (-10.0, -float(self.paddle_width))
        )

        new_left = tuple([tuple([y, x - self.paddle_width]) for y, x in left_half_circle])

        new_right = tuple([tuple([y, x + self.paddle_width]) for y, x in right_half_circle])

        s.addcomponent(middle_part, "white", "white")
        s.addcomponent(new_left, "white", "white")
        s.addcomponent(new_right, "white", "white")
        register_shape("myshape", s)
