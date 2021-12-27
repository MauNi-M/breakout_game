from turtle import *

BODY_POS = (0,-250)
EDGES_POS_LR = ((20*-2.5,-250), (20*2.5, -250))

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
    (10.0, -40.0),
    (10.0, 40.0),
    (-10.0, 40.0),
    (-10.0, -40.0)
)

new_left = tuple([tuple([y, x - 40]) for y, x in left_half_circle])

new_right = tuple([tuple([y, x + 40]) for y, x in right_half_circle])

s.addcomponent(middle_part, "black", "black")
s.addcomponent(new_left, "white", "black")
s.addcomponent(new_right, "white", "black")
register_shape("myshape", s)

class Paddle(Turtle):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body_xpos = 0
        self.body_ypos = -250
        self.r_edge_xpos = 2.5 * 20 + self.body_xpos
        self.l_edge_xpos = -2.5 * 20 - self.body_xpos
        # body
        self.body = Turtle()
        self.body.shape("square")
        self.body.shapesize(stretch_len=5)
        self.body.color("white", "white")
        self.body.penup()
        self.body.setposition(x=self.body_xpos, y=self.body_ypos)
        # edges
        self.l_edge = Turtle()
        self.l_edge.penup()
        self.l_edge.shape("circle")
        self.l_edge.color("white", "white")
        self.l_edge.setposition(x=self.l_edge_xpos, y=self.body_ypos)

        self.r_edge = Turtle()
        self.r_edge.penup()
        self.r_edge.shape("circle")
        self.r_edge.color("white", "white")
        self.r_edge.setposition(x=self.r_edge_xpos, y=self.body_ypos)


    def move_paddle(self, x_pos):
        if -320 < x_pos < 320:
            self.body_xpos = x_pos
            self.body.setx(self.body_xpos)
            self.update_edges_pos()
        else:
            print(f"mouse out of bounds: {x_pos}")


    def update_edges_pos(self):
        self.r_edge_xpos = 2.5 * 20 + self.body_xpos
        self.l_edge_xpos = -2.5 * 20 + self.body_xpos
        self.r_edge.setx(self.r_edge_xpos)
        self.l_edge.setx(self.l_edge_xpos)