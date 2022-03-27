from sense_hat import SenseHat
from time import sleep
import random

sense = SenseHat()

# Define some colours — keep brightness low
g = [0,128,0]
o = [0,0,0]

# Define a simple image
image = [
    g,g,g,g,g,g,g,g,
    o,g,o,o,o,o,g,o,
    o,o,g,o,o,g,o,o,
    o,o,o,g,g,o,o,o,
    o,o,o,g,g,o,o,o,
    o,o,g,g,g,g,o,o,
    o,g,g,g,g,g,g,o,
    g,g,g,g,g,g,g,g,
]

# Define a function to update the LED matrix
def active_status():
    # A list with all possible rotation values
    rotation_values = [0,90,180,270]
    # Pick one at random
    rotation = random.choice(rotation_values)
    # Set the rotation
    sense.set_rotation(rotation)

# Display the image
sense.set_pixels(image)
while True:
    # Do stuff (in this case, nothing)
    sleep(2)
    # Update the LED matrix
    active_status(