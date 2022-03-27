# from https://projects.raspberrypi.org/en/projects/code-for-your-astro-pi-mission-space-lab-experiment/3

from sense_hat import SenseHat

sense = SenseHat()
sense.color.gain = 16
light = sense.color.clear
if light < 64:
    print('Dark')
else:
    print('Light')