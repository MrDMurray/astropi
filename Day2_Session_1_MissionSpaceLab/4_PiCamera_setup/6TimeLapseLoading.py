from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

for i in range(3*60):
    camera.capture(f'image_{i:03d}.jpg')  # Take a picture every minute for 3 hours
    sleep(60)

    # Every 2 iterations, it will print a # to show it's still working away
    if i%2 == 0:
        print('#' , end='') # end = '' allows you to print on the same line
    
    # Every 30 iterations, it will say how many minutes left, total - i
    if i%30 == 0:
        print('- \n',180 - i,"mins left")
    
    # Just before the last iteration, it'll say it's done.
    if i == 179:
        print("\n All done!")