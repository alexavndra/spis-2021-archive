# individual warmup for lab05

from PIL import Image

# creates an object out of the bear.png
bear = Image.open("bear.png")

# prints the dimensions of the picture
(width, height) = bear.size

# gets the pixel of the bear at the specific x,y (tuple)
pixel = bear.getpixel( (100, 200 ))

# prints the RGB color of the pixel at that x,y 
print(pixel)

# replaces pixel at x,y with certain RGB
bear.putpixel( (100, 200), (0, 0, 0) )

# visibility of the black pixels on picture
for i in range(100):
  bear.putpixel( (i, 200) , (0, 0, 0) )

# create/overwrite tmp_Name.png with current image
bear.save("tmp_alex.png") 



def invert(im):

    ''' Invert the colors in the input image, im '''

    # Find the dimensions of the image

    (width, height) = im.size

   # Loop over the entire image

    for x in range( width ):

        for y in range( height ):

            (red, green, blue, op) = im.getpixel((x, y))

            im.putpixel((x,y), (255 - red, 255 - green, 255 - blue,op - 0))

            # Complete this function by adding your lines of code here.

            # You need to calculate the new pixel values and then to change them

            # in the image using putpixel()

    im.save("newnew.png")         

def invert_block(im):

    ''' Invert the colors in the input image, im, by only modding part of the image '''

    # Find the dimensions of the image

    (width, height) = im.size

   # Loop over the entire image

    for x in range( width // 2, width ):

        for y in range( height // 2 ):

            (red, green, blue, op) = im.getpixel((x, y))

            im.putpixel((x,y), (255 - red, 255 - green, 255 - blue, op - 0))

    im.save("invertedblock.png")   


# invert(bear) 
invert_block(bear)         