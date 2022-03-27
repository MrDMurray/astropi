# DgenerationEx code

# Niamh and Fionn

# Looking for changes in rivers over time

from logzero import logger, logfile
from ephem import readtle, degree
from picamera import PiCamera
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
import csv

dir_path = Path(__file__).parent.resolve()

# giving the log a name
logfile(dir_path/"DegenerationEx.log")

# What's up with TLE ISS
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"
iss = readtle(name, line1, line2)

# Set up planet selfie stick
cam = PiCamera()
cam.resolution = (2592, 1944)

def create_csv_file(data_file):
    """Create a new CSV file and add the header row"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Temperature", "Humidity")
        writer.writerow(header)

def add_csv_data(data_file, data):
    """Add a row of data to the data_file CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def get_latlon():
    """Return the current latitude and longitude, in degrees"""
    iss.compute() # Retrieve lat/long values from ephem
    return (iss.sublat / degree, iss.sublong / degree)


def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    iss.compute() # Get the lat/long values from ephem

    # earth portrait in 3...2...1
    camera.capture(image)


# initialise the CSV file
data_file = dir_path/"data.csv"
create_csv_file(data_file)
# initialise the photo counter
photo_counter = 1

# record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# run a loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=178)):
    try:

        # get latitude and longitude
        latitude, longitude = get_latlon()
        # Save the data to the file
        data = (
            datetime.now(),
            photo_counter,
            latitude,
            longitude
        )
        add_csv_data(data_file, data)
        # earth selfie
        image_file = f"{dir_path}/photo_{photo_counter:03d}.jpg"
        capture(cam, image_file)
        logger.info(f"iteration {photo_counter}")
        photo_counter += 1
        sleep(14)
        # what time is it
        now_time = datetime.now()
        
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))
        
print("Our program is complete")
