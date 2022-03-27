# 2 Imposters  (Aaron and Cameron) were looking at the changes of deforrestations through out the year and comparing it to the previous years

# We are not using max resolution on the camera so that we can get more frequent photos 

from picamera import PiCamera
from ephem import readtle, degree
from datetime import datetime, timedelta
from time import sleep
from logzero import logger, logfile
from pathlib import Path
import csv

print("The program is starting now!")

# where my files are going to be
dir_path = Path(__file__).parent.resolve()

# Setting our team name
logfile(dir_path/"2 Imposters.log")

# Where the ISS location is at the moment
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"
iss = readtle(name, line1, line2)

# Set up your camera
cam = PiCamera()
#cam.resolution = (1296, 972)

def create_csv_file(data_file):
  # Makes spreadsheet
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "picknumber", "latitude/longitube")
        writer.writerow(header)

def add_csv_data(data_file, data):
  # add to the spreadsheet
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def get_latlon():
    iss.compute() # Get the lat/long values from ephem
    return (iss.sublat / degree, iss.sublong / degree)

def convert(angle):
    # Converts data for exif 
    degrees, minutes, seconds = (float(field) for field in str(angle).split(":"))
    exif_angle = f'{abs(degrees):.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return degrees < 0, exif_angle

def capture(camera, image):
    # Uses camera to capture images files, also puts in latitude/longitude data
    
    iss.compute() # this gets the lat/long values from ephem

    # Changes the format slighty using the convert function above
    south, exif_latitude = convert(iss.sublat)
    west, exif_longitude = convert(iss.sublong)

    # Does the EXIF tags
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # It captures the image
    camera.capture(image)


# Start the spreadsheet
data_file = dir_path/"data.csv"
create_csv_file(data_file)

# Record the start and current time
start_clock = datetime.now()
now_clock = datetime.now()

# Start the counterBrain (counterBrain is a ounter that counts photos and data and cycles)
counterBrain = 1

# Alot of my code will run for about 3 hours
while (now_clock < start_clock + timedelta(minutes=0.2)):
    try:
        # get latitude and longitude
        latitude, longitude = get_latlon()
        # Save the data to the spreadsheet
        data = (
            datetime.now(),
            counterBrain,
            latitude,
            longitude
        )
        add_csv_data(data_file, data)
        # capturing the image with counterBrain
        image_file = f"{dir_path}/photo_{counterBrain:03d}.jpg"
        capture(cam, image_file)
        logger.info(f"cyclepoint {counterBrain}")
        counterBrain += 1
        sleep(5)
        # update the current clock time
        now_clock = datetime.now()
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))
        
print('my destiny is fulfilled, project complete')
#say hello finn and freya murray, thank you:)
