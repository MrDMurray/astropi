from picamera import PiCamera
from time import sleep

camera = PiCamera()
#camera.resolution = (2592, 1944)

# show what the camera sees for 30 seconds to allow you to focus it
try:
    camera.start_preview()
    sleep(30)
    camera.stop_preview()

# Press CTRL + C to stop the preview if you're all done
except:
    camera.stop_preview()