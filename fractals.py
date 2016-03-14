# Fractals
import turtle

my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.setpos(-300, 200)
my_turtle.pendown()


def algorithm_koch_curve(koch_turtle, length, degree):
    for x in range(3):
        algorithm_koch_curve_recur(koch_turtle, length, degree)
        koch_turtle.right(120)


def algorithm_koch_curve_recur(koch_turtle, length, degree):
    if degree == 0:
        koch_turtle.forward(length)
    else:
        length /= 3
        degree -= 1
        algorithm_koch_curve_recur(koch_turtle, length, degree)  # First segment
        koch_turtle.left(60)
        algorithm_koch_curve_recur(koch_turtle, length, degree)  # Second segment
        koch_turtle.right(120)
        algorithm_koch_curve_recur(koch_turtle, length, degree)  # Third segment
        koch_turtle.left(60)
        algorithm_koch_curve_recur(koch_turtle, length, degree)  # Fourth segment


def serpinski_tri(ser_turtle, length, degree, top_position):
    if degree == 0:
        pass
    else:
        degree -= 1

        for x in range(3):
            ser_turtle.forward(length)
            ser_turtle.right(120)
        serpinski_tri(ser_turtle, length / 2, degree, top_position)

        ser_turtle.penup()
        ser_turtle.setpos(top_position)
        ser_turtle.forward(length)
        ser_turtle.pendown()
        new_position = ser_turtle.pos()

        for x in range(3):
            ser_turtle.forward(length)
            ser_turtle.right(120)
        serpinski_tri(ser_turtle, length / 2, degree, new_position)

        ser_turtle.penup()
        ser_turtle.setpos(top_position)
        ser_turtle.right(60)
        ser_turtle.forward(length)
        ser_turtle.pendown()
        ser_turtle.left(60)
        new_position = ser_turtle.pos()

        for x in range(3):
            ser_turtle.forward(length)
            ser_turtle.right(120)
        serpinski_tri(ser_turtle, length / 2, degree, new_position)

"draw the triangles a stage at a time. draw 3, this will make the outer triangle, then continue downwards"
# algorithm_koch_curve(my_turtle, 200, 3)

position = my_turtle.pos()
serpinski_tri(my_turtle, 200, 5, position)
