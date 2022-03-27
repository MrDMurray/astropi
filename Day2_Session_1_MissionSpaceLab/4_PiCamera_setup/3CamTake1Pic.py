from picamera import PiCamera
from time import sleep

camera = PiCamera()

# shows what the camera sees
camera.start_preview()

print("Say cheese!")

# saves a picture
camera.capture('FirstPic.jpg')  # Take a picture

# stops showing what the camera sees
camera.stop_preview()

print("Oh wow! You look great today.")