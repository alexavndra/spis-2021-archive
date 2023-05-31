#Leah Kuruvila
#a program to draw the first letter of my name

import turtle



def draw_L(the_turtle):

  """Creates a function that will draw the letter 'L' when it takes in a parameter of a turtle """
  
  the_turtle.speed(1) #slows down turtle

  the_turtle.right(90)

  the_turtle.forward(100)

  the_turtle.left(90)

  the_turtle.forward(100)

  the_turtle.penup()

#my_turtle = turtle.Turtle()  # Create a new Turtle object

#draw_L(my_turtle)    # make the new Turtle draw the shape

newTurtle1 = turtle.Turtle() #creates new turtle object 
newTurtle1.penup() #pen up in order to set position without drawing
newTurtle1.setpos(-20, -20) #sets new position to differentiate between two turtles created
newTurtle1.down() 
draw_L(newTurtle1)


newTurtle2 = turtle.Turtle() #creates second turtle object
newTurtle2.penup() #pen up in order to set position without drawing
newTurtle2.setpos(10, 10) #sets new position to differentiate between two turtles created
newTurtle2.down()
draw_L(newTurtle2)