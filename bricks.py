from turtle import *
from random import randint, choice

colors = []
n = 10
INITIAL_POSITION = (-380, 200)
SCREEN_WIDTH = 800
NUMBER_OF_COLUMNS = 10
NUMBER_OF_ROWS = 5
BRICK_STRETCH_FACTOR = 20.5
for i in range(n):
    colors.append('#%06X' % randint(0, 0xFFFFFF))


class BrickBoard(object):

    def __init__(self):
        self.bricks = []
        self.brick_width = 0
        self.create_bricks(NUMBER_OF_COLUMNS, NUMBER_OF_ROWS)

    def create_bricks(self, columns, rows):
        brick_width = ((SCREEN_WIDTH - 40) // columns)
        self.brick_width = brick_width
        brick_height = 20
        init_x, init_y = INITIAL_POSITION

        for row in range(rows):
            new_y = init_y - (brick_height + 2) * row
            for column in range(columns):
                new_x = init_x + brick_width//2 + brick_width * column
                self.add_brick(coordinates=(new_x, new_y), brick_width=brick_width)

    def add_brick(self, coordinates, brick_width):
        brick = BreakOutBrick(x_pos=coordinates[0], y_pos=coordinates[1], b_height=20, b_width=brick_width)
        self.bricks.append(brick)

    def break_brick(self, brick: Turtle):
        brick.hideturtle()
        self.bricks.remove(brick)

    def out_of_bricks(self):
        if len(self.bricks) == 0:
            return True
        else:
            return False


class BreakOutBrick(Turtle):

    def __init__(self, x_pos, y_pos, b_height, b_width, *args, **kwargs):
        super().__init__(*args, **kwargs)
        border_coordinates = []
        self.shape("square")
        self.shapesize(stretch_len=b_width / BRICK_STRETCH_FACTOR)
        self.color(choice(colors))
        self.penup()
        self.x_center = x_pos
        self.y_center = y_pos
        self.brick_height = b_height
        self.brick_width = b_width
        self.setposition(self.x_center, self.y_center)
        self.x0 = self.x_center - self.brick_width // 2
        self.y0 = self.y_center + self.brick_height // 2
        self.x2 = self.x_center + self.brick_width // 2
        self.y2 = self.y_center - self.brick_height // 2

        self.upper_border = (((self.x0, self.y0), (self.x0+self.brick_width, self.y0)), False, False)
        self.lower_border = (((self.x2 - self.brick_width, self.y2), (self.x2, self.y2)), False, True)
        self.left_border = (((self.x0, self.y0-self.brick_height), (self.x0, self.y0)), True, False)
        self.right_border = (((self.x2, self.y2), (self.x2, self.y2+self.brick_height)), True, True)


