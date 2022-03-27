# Fun things to add to your code

### Every 5th iteration notify the user

```python
if photonumber % 5 == 0:
  print("it's working")
```
  
### Ascii ART

```python
print(" ")
print("   _      _      _           ")
print(" >(.)__ <(.)__ =(.)__        ")
print("  (___/  (___/  (___/  hjw   ")
print("                             ")
print("    OUR GROUP NAME           ")
```

## Loading 45% complete indicator

```python

# this program gives you the percentage complete in a loop like a loading bar

# WARNING: On THONNY, it won't overwrite the previous line like it's supposed to. That's a Thonny bug.
# If you run using CTR+T to run in the terminal, it works fine. 

from time import sleep


total_iterations = 30 # this is the bit you change to say how many cycles you want


for i in range(total_iterations):
    
    
    # Your code that is iterating goes here in place of the sleep
    sleep(0.1)
    
    
    percent_complete = round((i/total_iterations)*100,1) # calculates current completion % 
    
    print("Program is", percent_complete,"% Complete ", end = "\r") # prints it over the last line

print("program is complete!")


""" Example output:

 
Program is 6.7 % Complete
 
"""


```
 

### Watchdog Programs

eg. This program that shows the ISS crew a banner if there's a major incident and they're all exposed to the vacuum of space.

```python


from sense_hat import SenseHat

sense = SenseHat()
pressure = sense.get_pressure()
print("Pressure: %s Millibars" % pressure)

# checks if pressure in ISS is less than 300hPa
if pressure < 300: 


  sense.show_message("DON'T PANIC")

  print(" ")
  print(" ")
  print("  _____   ____  _   _ _ _______   _____        _   _ _____ _____   ")
  print("|  __ \ / __ \| \ | ( )__   __| |  __ \ /\   | \ | |_   _/ ____|   ")
  print(" | |  | | |  | |  \| |/   | |    | |__) /  \  |  \| | | || |       ")
  print(" | |  | | |  | | . ` |    | |    |  ___/ /\ \ | . ` | | || |       ")
  print(" | |__| | |__| | |\  |    | |    | |  / ____ \| |\  |_| || |____   ")
  print(" |_____/ \____/|_| \_|    |_|    |_| /_/    \_\_| \_|_____\_____|  ")
  print("                                                                   ")
                                                                 
  print("Space is 99.99% vacuum. If anything, THIS is far more normal by the standards of the universe.")
  
```  
  
## Sense Hat Logo Animations
  
```python

from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def trinket_logo():
    G = green
    Y = yellow
    B = blue
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, Y, Y, Y, B, G, O, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    Y, Y, Y, Y, Y, B, G, O,
    O, Y, Y, Y, B, G, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def raspi_logo():
    G = green
    R = red
    O = nothing
    logo = [
    O, G, G, O, O, G, G, O, 
    O, O, G, G, G, G, O, O,
    O, O, R, R, R, R, O, O, 
    O, R, R, R, R, R, R, O,
    R, R, R, R, R, R, R, R,
    R, R, R, R, R, R, R, R,
    O, R, R, R, R, R, R, O,
    O, O, R, R, R, R, O, O,
    ]
    return logo

def plus():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, W, W, O, O, O,
    O, O, O, W, W, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def equals():
    W = white
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O, 
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, W, W, W, W, W, W, O,
    O, W, W, W, W, W, W, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

def heart():
    P = pink
    O = nothing
    logo = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, P, P, O, O,
    P, P, P, P, P, P, P, O,
    P, P, P, P, P, P, P, O,
    O, P, P, P, P, P, O, O,
    O, O, P, P, P, O, O, O,
    O, O, O, P, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]
    return logo

images = [trinket_logo, trinket_logo, plus, raspi_logo, raspi_logo, equals, heart, heart]
count = 0

while True: 
    s.set_pixels(images[count % len(images)]())
    time.sleep(.75)
    count += 1
    
```
  
  
