#Leah Kuruvila
#a program to get familiar with the Turtle

import turtle

def draw_picture(the_turtle):

    ''' Draw a simple picture using a turtle '''

    the_turtle.forward(100) #moves turtle forward 100

    the_turtle.left(90) #turn turtle left 90 degrees

    the_turtle.forward(100)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(90)

    the_turtle.forward(100)

    the_turtle.left(90)    



my_turtle = turtle.Turtle()  # Create a new Turtle object

draw_picture(my_turtle)      # make the new Turtle draw the shape

turtle1 = turtle.Turtle() #creates new turtle object

turtle2 = turtle.Turtle() #creates new turtle object

turtle1.setpos(-50, -50) #makes turtle jump to new coordinates on the plane

turtle2.setpos(200, 100)

turtle1.forward(100)

turtle2.left(90)

turtle2.forward(100)