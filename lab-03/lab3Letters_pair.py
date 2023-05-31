# What is the “anonymous turtle”?
# the "anonymous turtle" is the default turtle(?)

# In the code below, what is the difference between turtle and Turtle()?
  # my_turtle = turtle.Turtle()
  # draw_picture(my_turtle)   
# the difference is that turtle is name of the package that contains all of the functions in Turtle and Turtle() is a function that allows the user to create a new Turtle object

# Imagine that I have a turtle in a variable named my_turtle. What line of code will change that turtle’s y-position to 100?
# my_turtle.sety(100)

import turtle

def draw_L(the_turtle, size):

  """Creates a function that will draw the letter 'L'at a specific size when it takes in a parameter of the turtle and size"""
  the_turtle.penup()

  the_turtle.setpos(-50,70)

  the_turtle.speed(1) #slows down turtle

  the_turtle.pendown()

  the_turtle.pensize(size)

  the_turtle.right(90)

  the_turtle.forward(100)

  the_turtle.left(90)

  the_turtle.forward(100)

  the_turtle.penup()

testTurtle = turtle.Turtle()
draw_L(testTurtle, 5)
