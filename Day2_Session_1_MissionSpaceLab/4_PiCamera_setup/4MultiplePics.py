from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

# shows what the camera sees
camera.start_preview()

print("Say triple cheese!")

# 3 pictures 1 second apart and name them
for eachPicNumber in range(3):
    camera.capture(f'image_{eachPicNumber:03d}.jpg')  
    sleep(1)
    print("snap")

# stops showing what the camera sees
camera.stop_preview()

print("And that was the story of the Three Little Pics.")


