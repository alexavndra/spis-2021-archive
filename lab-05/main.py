from PIL import Image
import random

print("Running lab05Warmup_alex.py") 
# let us know it's running lab05Warmup_alex.py

import lab05Warmup_alex              
# this will cause lab05Warmup_alex.py to run

print("Running lab05Warmup_leah.py")  
# let us know it's running lab05Warmup_leah.py

import lab05Warmup_leah               
# this will cause lab05Warmup_leah.py to run

# grayscales the image when called
def grayscale(im):

  (width, height) = im.size

  for x in range (width):

    for y in range (height):
      
      (red, green, blue, op) = im.getpixel((x, y))

      grayscaler = int((red + green + blue) // 3)
      im.putpixel((x,y), (grayscaler, grayscaler, grayscaler, op))

  im.save("grayscaled.png")


def binarize(im, thresh, startx, starty, endx, endy):

  (width, height) = im.size

  if startx > width:
    print("startx not sufficient for binarizing")
    return
  elif endx > width:  
    print("endx not sufficient for binarizing")
    return
  if starty > height:
    print("starty not sufficient for binarizing")
    return
  elif endy > height:  
    print("endy not sufficient for binarizing")
    return

  for x in range (startx, endx):

    for y in range (starty, endy):
      
      (red, green, blue, op) = im.getpixel((x, y))

      luminance = int((red + green + blue) // 3)

      if luminance > thresh:

        im.putpixel((x,y), (255, 255, 255, op))

      elif luminance < thresh:

        im.putpixel((x,y), (0, 0, 0, op))  

  im.save("binarized.png")


def mirrorVert(im):

  (width, height) = im.size 

  for x in range (width):

    for y in range (height) :
      
      (red, green, blue, op) = im.getpixel((x, y))
      im.putpixel((x, (height - y - 1)), (red, green, blue, op))

  im.save("mirrorVert.png")    


def mirrorHoriz(im):

  (width, height) = im.size  

  for x in range (width):

    for y in range (height):
      
      (red, green, blue, op) = im.getpixel((x, y))
      im.putpixel((width - x - 1, y), (red, green, blue, op))

  im.save("mirrorHoriz.png")   


def flipVert(im):

  (width, height) = im.size

  for x in range (width):
    
    for y in range (height // 2):

      sourcepixel = im.getpixel((x,y))
      endpixel = im.getpixel((x, height - y - 1))
      im.putpixel((x,y), endpixel)
      im.putpixel((x,height - y - 1), sourcepixel)
      
  im.save("flipVert.png")


def scale(im):

  (width, height) = im.size
  image1 = Image.new('RGB', (width, height))

  for x in range(im.size[0] // 2):

    for y in range(im.size[1] // 2):

      (r, g, b, op) = im.getpixel((x * 2, y * 2))
      image1.putpixel((x,y), (r, g, b, op))

  return image1    

def blur(im):

  (width, height) = im.size
  image1 = Image.new('RGB', (width, height))
  x = 0
  y = 0

  while x < width:
    y = 0
    while y < height:
      total = [0,0,0,0]

      for i in range(x, x + 5):
        
        for z in range(y, y + 5):
          
          if i < width and z < height:

            (red, green, blue, op) = im.getpixel((i, z))

            #pixel = int(red + green + blue)
            total[0] = total[0] + red
            total[1] = total[1] + green
            total[2] = total[2] + blue
            total[3] = total[3] + op
            
      average = [0,0,0,0]
      average[0] = total[0] // 25
      average[1] = total[1] // 25
      average[2] = total[2] // 25
      average[3] = total[3] // 25

      for i in range(x,x + 5):

        for z in range (y, y + 5):
        
          if i < width and z < height:
    
            image1.putpixel((i,z), (average[0], average[1], average[2],average[3]))
      y = y + 5
    x = x + 5
  return image1


def randomGrid(im):  
  
  (width, height) = im.size
  image1 = Image.new('RGB', (width, height))
  
  mini_image_width = width // 4
  mini_image_height = height // 3

  locationList = [] # top left of the mini image

  # need to do an n x n grid (need a variable?)
  # 3 x 4 grid?
  # random.choices()
  # make new images and then put it all together in the end
  # adjustable ranges(??)

  for x in range (0,width,mini_image_width):

    for y in range (0,height,mini_image_height):

      locationList.append((x,y))
  
  copy = list.copy(locationList)
  random.shuffle(locationList)
  num = 0 # references copy

  for i in locationList:
    
    a,b = copy[num][0],copy[num][1]

    for x in range (i[0], i[0] + mini_image_width,1):

    # mini_image = Image.new('RGB', (mini_image_width, mini_image_height))

      for y in range (i[1], i[1] + mini_image_height,1):
        
        if x >= width or y >= height or a >= width or b >= height:
          
          continue  
        
        (red, green, blue, op) = im.getpixel((x,y))
        
        # if red == 255 and green == 255 and blue == 255:
          
        #   continue

        image1.putpixel((a,b), (red, green, blue, op))
        b += 1
        # print(b)

      a += 1
      b = copy[num][1]
    
    if num == len(copy) - 1:
      
      return image1
    
    num += 1
    
  return image1      


# grayBear = Image.open("bear.png")  
# grayscale(grayBear)

# verticalBear = Image.open("bear.png") 
# mirrorVert(verticalBear)

# binarizeBear = Image.open("bear.png") 
# binarize(binarizeBear, 150, 0, 0, 470, 629)

# horizontalBear = Image.open("bear.png")
# mirrorHoriz(horizontalBear)

# flipVertBear = Image.open("bear.png")
# flipVert(flipVertBear)

# scaleBear = Image.open("bear.png")
# scale(scaleBear).save("scaled.png")

# blurredBear = Image.open("bear.png")
# blur(blurredBear).save("blur.png")
# print("blur")

gridBear = Image.open("bear.png")
randomGrid(gridBear).save("grid.png")
print("grid")

