#Fractals
import turtle
my_turtle = turtle.Turtle()
my_turtle.penup()
my_turtle.setpos(-300, 300)
my_turtle.pendown()
turtle.speed(0)
def Algorithm_Koch_Curve(my_turtle, length, degree):
    
    if degree == 0:
        my_turtle.forward(length)
    else:
        length = length / 3
        degree -= 1
        Algorithm_Koch_Curve(my_turtle, length, degree) # First segment
        my_turtle.left(60)
        Algorithm_Koch_Curve(my_turtle, length, degree) # Second segment
        my_turtle.right(120)
        Algorithm_Koch_Curve(my_turtle, length, degree) # Third segment
        my_turtle.left(60)
        Algorithm_Koch_Curve(my_turtle, length, degree) # Fourth segment


##def serpinski_tri(turtle, length, degree):
##    for x in range(3):
##        turtle.forward(length)
##        my_turtle.right(120)
##
##    length = length /2
##    turtle.forward(length)
##    my_turtle.right(60)
##    position = turtle.pos()
##    recur_ser_tri(turtle, length, degree, position)
##    
##
##def recur_ser_tri(turtle, length, degree, position):
##    if degree == 0:
##        pass
##    else:
##        degree -= 1
##        for x in range(3):
##            turtle.forward(length/2)
##            position = turtle.pos()
##            recur_ser_tri(turtle, length/2, degree, position)
##            turtle.forward(length/2)
##            my_turtle.right(120)
##
##        length = length/2
##        my_turtle.left(60)
##        turtle.forward(length)
##        my_turtle.right(60)
##        my_turtle.penup()
##        my_turtle.setpos(position)
##        my_turtle.pendown()

"draw the triangles a stage at a time. draw 3, this will make the outer triangle, then continue downwards"
  
  

    
    

#Algorithm_Koch_Curve(my_turtle, 300, 3)
serpinski_tri(my_turtle, 400, 3)
