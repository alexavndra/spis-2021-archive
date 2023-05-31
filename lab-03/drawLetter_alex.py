# alexandra hernandez spis 2021
# drawing out first letter of my name using turtle

import turtle
import random

def draw_A(the_turtle):

  """" program will draw out the letter A based on the parameter of the turtle (calling the addressed turtle) """

  the_turtle.pensize(5)

  the_turtle.pd()

  the_turtle.speed(1) # slowing down the turtle speed to make sure you can see the A being drawn out by the turtle

  the_turtle.left(45)

  the_turtle.forward(100)

  the_turtle.right(90)

  the_turtle.forward(100)

  the_turtle.pu()

  the_turtle.backward(50)

  the_turtle.right(135)

  the_turtle.pd()

  the_turtle.forward(70)

alexTurtle1 = turtle.Turtle()
alexTurtle2 = turtle.Turtle()

alexTurtle1.pu()
alexTurtle1.pencolor("yellow")
alexTurtle1.setpos(-50,10)

alexTurtle2.pu()
alexTurtle2.pencolor("blue")
alexTurtle2.setpos(-50,-50)

draw_A(alexTurtle1)
draw_A(alexTurtle2)