# cImage - A simple image processing library for Python
# https://pypi.org/project/cImage/
# pip install cImage
# Then load "cImage" into Thonny
import time
import image

original_image = image.FileImage('EarthImage1Astro.jpg')

width = original_image.get_width()
height = original_image.get_height()
print(width, height)
win = image.ImageWin(width, height, "Image Processing") # set window to image size

original_image.draw(win)
my_image = original_image.copy()

timeStamp = round(time.time())
print(str(timeStamp))

print ("About to loop " + str(height * width) + " times, one for each pixel")
for row in range(height):
    for col in range(width):
         v = my_image.get_pixel(col,row)
         # Apply filter\ or processing of some form
         if (v.green < 100):
             v.red = 0
             v.green = 0
             v.blue = 0
         my_image.set_pixel(col,row,v)

print("Finished looping image !!")

my_image.draw(win)
print(win.get_mouse())
my_image.save('EImage_' + str(timeStamp) + '.jpg')
# print(my_image.to_list())
win.exit_on_click()