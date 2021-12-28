from turtle import Shape, register_shape

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

new_left = tuple([tuple([y, x - 60]) for y, x in left_half_circle])

new_right = tuple([tuple([y, x + 60]) for y, x in right_half_circle])

s.addcomponent(middle_part, "black", "black")
s.addcomponent(new_left, "white", "black")
s.addcomponent(new_right, "white", "black")
register_shape("myshape", s)


