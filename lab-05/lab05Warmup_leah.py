from PIL import Image

bear = Image.open( "bear.png" )
#image is composed of 600 x 800 pixels
#size = bear.size
#print(size)


pixel = bear.getpixel( ( 100, 200) )
print(pixel)

for i in range(100):
  bear.putpixel( (i, 200) , (0, 0, 0) )

bear.save( "tmp_leah.png" )



def invert( im ):

    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image
    (width, height) = im.size


    # Loop over the entire image
    for x in range( width ):

        for y in range( height ):

            (red, green, blue, op) = im.getpixel((x, y))

            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them

            im.putpixel( (x,y) , (225 - red, 225 - green, 225 - blue, op - 0) )

            # in the image using putpixel()

    
    im.save( "invertimage.png" )

def invert_block( im ):

  ''' only inverts the pixels that are in the upper-right quadrant of the image '''

  # Find the dimensions of the image
  (width, height) = im.size

  # Loop over the entire image
  for x in range( width // 2 , width ):

        for y in range( height // 2 ):

            (red, green, blue, op) = im.getpixel((x, y))

            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them

            im.putpixel( (x,y) , (225 - red, 225 - green, 225 - blue, op - 0) )

            # in the image using putpixel()

  im.save("invertedblockimage.png")



#invert(bear)
invert_block(bear)