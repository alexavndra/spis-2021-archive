# recursive tree

import turtle

# The function takes as arguments: a trunk_length which is the length of the main trunk of the tree, and the height indicating the number of levels of branching of the tree.
drawing = turtle.Turtle()

def draw_branch(turtle, trunk_length, height):
  
  if height < 1 :
    return

  turtle.forward(trunk_length) # move
    
  if height > 1 :

    # draw left branch
    turtle.left(60)
    draw_branch(drawing, trunk_length - 7, height - 1)

    # draw right branch
    turtle.right(60)
    draw_branch(drawing, trunk_length - 7, height - 1) 

    turtle.right(60)
    draw_branch(drawing, trunk_length - 7, height - 1) 
  
    # restore turtle direction 
    turtle.left(60)

  turtle.backward(trunk_length)

def draw_tree(trunk_height) :
  
  drawing.speed(0)

  drawing.setheading(90)
  drawing.backward(trunk_height)
  draw_branch(drawing, trunk_height, 5)

  turtle.exitonclick()


draw_tree(50) 