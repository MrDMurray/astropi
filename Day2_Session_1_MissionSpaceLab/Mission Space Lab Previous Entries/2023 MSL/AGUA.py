#Team Bronze

from pathlib import Path
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

'''
__________                                     
\______   \_______  ____   ____ ________ ____  
 |    |  _/\_  __ \/  _ \ /    \\___   // __ \ 
 |    |   \ |  | \(  <_> )   |  \/    /\  ___/ 
 |______  / |__|   \____/|___|  /_____ \\___  >
        \/                    \/      \/    \/ 
Team Bronze
Classifying cloud types using ML using data obtained from snapping the earth for 3 hours (Fully Tested!)
Abigail Bosch & Stephen Flynn
St Josephs Rush, Dublin, Ireland, Planet Earth, Milky Way Galaxy
2022

Well here it is, we made it to orbit before Bezos! We have a few things we'd like to say but thanks to Danny Murray for setting this up, legend.

Abigails Message:
But, Moon, and Star,
Though you're very far-,
There is one - farther than you-,
She - is more than a firmament - from Me -
So I can never go!
- Emily Dickisnon

Stephens Message:
Well better put something nice on this yoke,
Bridie, Rose, thank you!
Stephen was here.


"I serisously can't beat that with...Like I made a Jeff Bezos joke and you did a poem lmao" - Stephens message to Abigail after comparing our messages.

'''

def make_the_csv_file(data_stored_directory):
    """Create a new CSV file and add the header row"""
    with open(data_stored_directory, 'w') as f:
        writer = csv.writer(f)
        header = ("Counter", "Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
        writer.writerow(header)

def plus_data_from_csv(data_stored_directory, data):
    """Add a row of data to the data_stored_directory CSV"""
    with open(data_stored_directory, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def calculate_angle(angle):
    """
    Work out a `skyfield` Angle and make it EXIF-appropriate
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    location = ISS.coordinates()

    # calculate_angle the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = calculate_angle(location.latitude)
    west, exif_longitude = calculate_angle(location.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # capture the image
    camera.capture(image)


base_folder = Path(__file__).parent.resolve()

# Set a logfile name
logfile(base_folder/"events.log")

# Set up Sense Hat
sense = SenseHat()

# Set up camera
cam = PiCamera()
cam.resolution = (4056, 3040) # Full throttle! (Don't worry, testing came out <3GB)

# Initialise the CSV file
data_stored_directory = base_folder/"data.csv"
make_the_csv_file(data_stored_directory)

# Initialise the photo counter
counter = 1
# Record the start and current time
begin_experiment = datetime.now()
current_time = datetime.now()
# Run a loop for (almost) three hours
while (current_time < begin_experiment + timedelta(minutes=161)): # 161 as 178 sometimes went over in testing
    try:
        humidity = round(sense.humidity, 4)
        temperature = round(sense.temperature, 4)
        # Get coordinates of location on Earth below the ISS
        location = ISS.coordinates()
        # Save the data to the file
        data = (
            counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            temperature,
            humidity,
        )
        plus_data_from_csv(data_stored_directory, data)
        # capture image
        image_file = f"{base_folder}/photo_{counter:03d}.jpg"
        capture(cam, image_file)
        # Log event
        logger.info(f" is on iteration {counter} of about 470 or so. All good.")
        counter += 1
        sleep(20) # 20 as opposed to 30 or 60. This number came from hours of testing in bright light.
        # Update the current time
        current_time = datetime.now()
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')

