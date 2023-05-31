# recursive spiral

import turtle

# angle = degrees

def spiral(initial_length, angle, multiplier):

  turtlePen.speed(1)

  if initial_length < 1:
    return

  turtlePen.forward(initial_length)
  turtlePen.right(angle)
  spiral(initial_length * multiplier, angle, multiplier)


turtlePen = turtle.Turtle()  
spiral(120, 45, 0.9)
turtle.exitonclick() 

# The spiral should stop drawing when it has reached a side length of less than 1 pixel (if multiplier<1) or greater than 200 pixels (if multiplier>1). this depends on whether you're drawing out-in or in-out

