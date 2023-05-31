import turtle
import csv

def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.gif")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    
    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

        

def irma():
    """Animates the path of hurricane Irma
    """
    # Do not change this line
    # t is the turtle, and you will not need the other variables
    (t, wn, map_bg_img) = irma_setup()

    hurricaneFile = "data/irma.csv"
    # The line below is a little magical. It opens the file,
    # with awareness of any errors that might occur.
    with open(hurricaneFile, 'r') as csvfile:
        # This line gives you an "iterator" you can use to get each line
        # in the file.
        pointreader = csv.reader(csvfile)
        
        # "Date: Date Time: Time" is header
        pointreader = iter(pointreader)
        next(pointreader)

        t.penup()

        # You'll need to add some code here, before the loop
        # One thing you'll need to figure out how to do is to
        # skip the first line of the file (which is the header).
        # You might use a boolean variable, or you can
        # look into Python's built-in next function
        #(https://docs.python.org/3/library/functions.html#next)
        # pointreader is an iterator

        for row in pointreader:
            # row is a list representing each line in the csv file
            # Each comma separated element is in its own index position
            # This code just prints out the date and time elements of each
            # row in the file.
            # Make sure you understand what is happening here.
            # Then, you'll need to change this code
            t.setpos(float(row[3]), float(row[2]))
            drawingTemplate(t, int(row[4]))

            print("Date:", row[0], "Time:", row[1], "Lat:", row[2], "Long:", row[3], "Wind:", row[4])



    # Hack to make sure a reference to the background image stays around
    # Do not remove or change this line
    return map_bg_img


# Feel free to add "helper" functions here

# drawingTemplate function; helper function for the irma loop
# parameters are the turtle and wind
# turtle = hurricane tracker
# wind = speed (casted into a float when it's called in irma function)

def drawingTemplate(turtle, wind):
  
  """ adjusts the pencolor and pen size of the hurricane based on the wind speed """
  
  turtle.pendown()

  if wind > 155 : # catastropic (cat 5)
    turtle.pencolor("red")
    turtle.pensize(20)
  elif wind > 131 and wind < 155 : # extreme (cat 4)
    turtle.pencolor("orange")
    turtle.pensize(15)
  elif wind > 111 and wind < 130 : # extensive (cat 3)
    turtle.pencolor("yellow")
    turtle.pensize(10)  
  elif wind > 96 and wind < 110 : # moderate (cat 2)
    turtle.pencolor("green")
    turtle.pensize(6)  
  elif wind > 74 and wind < 95 : # minimal (cat 1)
    turtle.pencolor("blue")
    turtle.pensize(4) 
  elif wind < 74 : # nothing (cat 0?)
    turtle.pencolor("white")
    turtle.pensize(2)   

if __name__ == "__main__":
    bg=irma()

turtle.exitonclick() 