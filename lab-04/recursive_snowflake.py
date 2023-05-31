# recursive snowflake

import turtle

drawing = turtle.Turtle()

def single_snowflake(side_length, levels):
  for angle in [-120, -120, 0]:
    snowflake_side(side_length, levels)
    drawing.left(angle)


# recursion will take place here
def snowflake_side(side_length, levels):

  if levels == 0: 
    drawing.forward(side_length)
  else:
    snowflake_side(side_length // 3, levels - 1)
    drawing.left(60)

    snowflake_side(side_length // 3, levels - 1)
    drawing.left(-120)

    snowflake_side(side_length // 3, levels - 1)
    drawing.left(60)

    snowflake_side(side_length // 3, levels - 1)
    drawing.left(0)

drawing.penup()
drawing.speed(1)
drawing.pendown()
single_snowflake(100, 3)

turtle.exitonclick()  