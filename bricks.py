from turtle import *
from random import randint, choice

colors = []
n = 10
INITIAL_POSITION = (-380, 200)
SCREEN_WIDTH = 800

for i in range(n):
    colors.append('#%06X' % randint(0, 0xFFFFFF))


class BrickBoard(object):

    def __init__(self):
        self.bricks = []
        self.create_bricks(10, 10)

    def create_bricks(self, columns, rows):
        brick_width = ((SCREEN_WIDTH - 40) // columns)
        brick_height = 20
        init_x, init_y = INITIAL_POSITION

        for row in range(rows):
            new_y = init_y - (brick_height + 5) * row
            for column in range(columns):
                new_x = init_x + brick_width//2 + brick_width * column
                self.add_brick(coordinates=(new_x, new_y), brick_width=brick_width)

    def add_brick(self, coordinates, brick_width):
        brick = Turtle(shape="square")
        brick.shapesize(stretch_len=brick_width // 20)
        brick.color(choice(colors))
        brick.penup()
        brick.setposition(coordinates)
        self.bricks.append(brick)
