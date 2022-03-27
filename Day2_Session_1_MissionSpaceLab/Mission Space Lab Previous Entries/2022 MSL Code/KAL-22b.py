# Team KAL-22b

from pathlib import Path
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

"""
This program will capture a scattergun array of images.
These will be processed back on earth to test our machine learning algorithm. We will then test
to see if biomes can be classified. Very exciting!
This project is made by Allison Joyce, Kamaya Gogna and Lily Carrick.
We took part in this project because we are very interested in space and coding. We would like to say hello to our friends, family, pets and a big shoutout
to St Josephs Secondary School. A special shoutout to Mr Murray who gave us this wonderful opportunity.
(kumud) my sister

Fully tested, under 3 gigs and runs for less than 3 hours. Go for launch!

        ||            /_\
    \_______/         | |
                      | |
                       =
                      !!!
"""

def conjour_me_a_csv_file(numbers_folder):
    """whip up a new csv file with a top row"""
    with open(numbers_folder, 'w') as f:
        writer = csv.writer(f)
        header = ("count_dracula", "Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
        writer.writerow(header)

def add_csv_data(numbers_folder, data):
    """New row of numbers to the numbers_folder CSV """
    with open(numbers_folder, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Change the angle format
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Get a picture and put it 'location_data' ."""
    location = ISS.coordinates()

    south, exif_latitude = convert(location.latitude)
    west, exif_longitude = convert(location.longitude)

    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    camera.capture(image)


base_folder = Path(__file__).parent.resolve()

# Set a logfile name to strange_happenings
logfile(base_folder/"strange_happenings.log")

# Set up our sensible Sense Hat
sense = SenseHat()

# Set up our snazzy camera and set it to higher res (this is tested and still under 3GB)
# 
cam = PiCamera()
cam.resolution = (4056, 3040) 

# Start the CSV file
numbers_folder = base_folder/"data.csv"
conjour_me_a_csv_file(numbers_folder)

# Start the photo count_dracula
count_dracula = 1

# Record the start and current time now
start_time = datetime.now()
now_time = datetime.now()

# Keep the program going for about three hours-ish
while (now_time < start_time + timedelta(minutes=160)):
    try:
        humidity = round(sense.humidity, 4)
        temperature = round(sense.temperature, 4)
        # Get coordinates
        location = ISS.coordinates()
        # Save the data 
        data = (
            count_dracula,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            temperature,
            humidity,
        )
        add_csv_data(numbers_folder, data)
        # capture image
        image_file = f"{base_folder}/photo_{count_dracula:03d}.jpg"
        capture(cam, image_file)
        # Log event
        logger.info(f"iteration {count_dracula}")
        count_dracula += 1
        sleep(20)
        # Update the current time
        now_time = datetime.now()
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')

