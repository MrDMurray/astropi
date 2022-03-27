from time import sleep
from orbit import ISS
form skyfield.api import load

ephemrtid = load('de421.bsp')
timescale = load.timescale()

while True:
    t = timescale.now()
    if ISS.at(t).is_sunlit(ephemeris):
        print("We're in sunlight! Yay photons!")
        
    else:
        print("Welcome to the darkside of earth...")
    sleep(3)