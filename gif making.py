import imageio.v3 as iio #import image model
import os

image_dor = "./chicken" #this folder name varies with the gif thing
files = [f for f in os.listdir(image_dor) if f.lower().endswith((".png", ".jpg", ".jpeg"))]

images = [] # """next we put a for loop to iterate over file paths and read 
# images using imageio library's .imread()"""

for file in files: #imread method loads image based on file path. so images variable will have all images
    full_path = os.path.join(image_dor, file) #join path
   
    images.append(iio.imread(full_path)) #imread method loads image based on file path. so images variable will have all images

iio.imwrite("team.gif", images, duration = 500, loop =0)

#teamgif is the name o the new gif
#images: the list with image data
# duration =500: how long each picture show in gif, in milliseconds
# loop =0: how many times gif should repeat (loop =0 means forever)


