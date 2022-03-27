# bluecobrascode

# Our code takes pictures so that we can compare the colour to the known temperatures of those parts of the ocean.

from time import sleep

print(" BLUE COBRA CODE RUNNING!  ")
print("              ____         ")
print("             / B B\        ")
print("             \  ----<      ")
print("              \  /         ")
print("    __________/ /          ")
print(" -=:___________/           ")
print(" Ethan, James, Todd, Daniel")

sleep(2)

from logzero import logger, logfile
from ephem import readtle, degree
from picamera import PiCamera
from datetime import datetime, timedelta
from pathlib import Path
import csv

dir_path = Path(__file__).parent.resolve()

# Lights Camera Action
phototaker = PiCamera()
phototaker.resolution = (2592, 1944)  # Max Res, fewer photos

# Broken Snakes Log
logfile(dir_path/"bluecobras.log")

# This is where i am 
# updated from http://www.celestrak.com/NORAD/elements/stations.txt on 19/02/21

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"
spaceportLocation = readtle(name, line1, line2)




# List of functions used by the program

def get_lonlat():
    # gets lat long for the ISS
    spaceportLocation.compute() # Get the lat/long values from ephem
    return (spaceportLocation.sublat / degree, spaceportLocation.sublong / degree)

def csvmaker(fileofdata):
    # makes a csv
    with open(fileofdata, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Temperature", "Humidity")
        writer.writerow(header)

def data_of_csv_added(fileofdatas, data):
    # adds to the csv
    with open(fileofdatas, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def make_that_change(angle): 
    #Converts angle using mathmatical magic
    degrees, minutes, seconds = (float(field) for field in str(angle).split(":"))
    exif_angle = f'{abs(degrees):.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return degrees < 0, exif_angle

def secure_the_moment(camera, picture):
    spaceportLocation.compute() # Get the lat/long values from ephem

    # convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = make_that_change(spaceportLocation.sublat)
    west, exif_longitude = make_that_change(spaceportLocation.sublong)

    # set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # capture the picture. Please work camera.
    camera.capture(picture)


# get the csv ready
data_file = dir_path/"data.csv"
csvmaker(data_file)

# initialise the photo counter and set the start and stop times
photo_counter = 1
start_time = datetime.now()
now_time = datetime.now()

# run a loop for (almost) three hours-ish
while (now_time < start_time + timedelta(minutes=177)):
    try: # really try python

        # get latitude and longitude
        latitude, longitude = get_lonlat()
        # Save the data to the file
        data = (
            datetime.now(),
            photo_counter,
            latitude,
            longitude
        )
        data_of_csv_added(data_file, data)
        # capture image
        image_file = f"{dir_path}/photo_{photo_counter:03d}.jpg"
        secure_the_moment(phototaker, image_file)
        logger.info(f"iteration {photo_counter}")
        photo_counter += 1
        sleep(15)

        # find what time it is now
        now_time = datetime.now()

    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))

print("I'm done, thanks!")
