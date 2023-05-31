# alexandra hernandez
# goal of program: try out turtle

import turtle

def draw_picture(the_turtle):
    ''' Draw a simple picture using a turtle '''

    the_turtle.forward(50) # moves turtle forward x amount

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(80) # degrees are used

    the_turtle.forward(100)

    the_turtle.left(100) # degrees are used

    the_turtle.forward(100)

    the_turtle.left(105) # degrees are used


my_turtle = turtle.Turtle()  # Create a new Turtle object

draw_picture(my_turtle)  # make the new Turtle draw the shape

turtle1 = turtle.Turtle() # creates new Turtle object

turtle2 = turtle.Turtle() # creates new Turtle object

turtle1.setpos(-50, -50) # sets new position of turtle 1

turtle2.setpos(200, 100) # sets new position of turtle 2

turtle1.forward(100)

turtle2.left(90)

turtle2.forward(100)
