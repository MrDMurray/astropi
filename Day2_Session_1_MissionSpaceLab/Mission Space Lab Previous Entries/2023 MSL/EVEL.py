# Team EVEL

from pathlib import Path
from logzero import logger, logfile
from sense_hat import SenseHat
from picamera import PiCamera
from orbit import ISS
from time import sleep
from datetime import datetime, timedelta
import csv

"""
Team EVEL is Eabha Mc Bride and Leah Mullen

Our program will take a scattergun array of images, these will be processed by our Coral Accelerator back on Earth
so that cloud types can be put into categories.

RESPONSE TO FEEDBACK: Thanks! We will transform the images when we get them back with photo editing software as you suggested.

TESTING: This program ran with no errors for under 3 hours and went for 466 iterations.
The output was under the 3GB limit (using bright daytime photos). 

"""
def make_file_for_csv(file_of_data):
    """Add top row to newly created CSV file"""
    with open(file_of_data, 'w') as f:
        writer = csv.writer(f)
        header = ("Cool_counter", "Date/time", "Latitude", "Longitude", "Temperature", "Humidity")
        writer.writerow(header)

def add_csv_data(file_of_data, data):
    """Add a row of data to the file_of_data CSV"""
    with open(file_of_data, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def convert(angle):
    """
    Convert skyfield angle
    """
    sign, degrees, minutes, seconds = angle.signed_dms()
    exif_angle = f'{degrees:.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return sign < 0, exif_angle

def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long EXIF data."""
    location = ISS.coordinates()

    # Convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(location.latitude)
    west, exif_longitude = convert(location.longitude)

    # Set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # Capture the image
    camera.capture(image)


base_folder = Path(__file__).parent.resolve()

# Set a logfile name
logfile(base_folder/"eventlogger.log")

# Set up Sense Hat
sense = SenseHat()

# Set up camera
cam = PiCamera()
cam.resolution = (4056, 3040) # FULL RES (it's cool, testing showed less than 3GB in total)

# Initialise the CSV file
file_of_data = base_folder/"data.csv"
make_file_for_csv(file_of_data)

# Initialise the photo Cool_counter
Cool_counter = 1
# Record the start and current time
start_time = datetime.now()
now_time = datetime.now()
# Run a loop for (almost) three hours
while (now_time < start_time + timedelta(minutes=160)):
    try:
        humidity = round(sense.humidity, 4)
        temperature = round(sense.temperature, 4)
        # Get coordinates of location on Earth below the ISS
        location = ISS.coordinates()
        # Save the data to the file
        data = (
            Cool_counter,
            datetime.now(),
            location.latitude.degrees,
            location.longitude.degrees,
            temperature,
            humidity,
        )
        add_csv_data(file_of_data, data)
        # Capture image
        image_file = f"{base_folder}/photo_{Cool_counter:03d}.jpg"
        capture(cam, image_file)
        # Log event
        logger.info(f"We're at photo {Cool_counter} of about 466ish.")
        Cool_counter += 1
        sleep(20)
        # Update the current time
        now_time = datetime.now()
    except Exception as e:
        logger.error(f'{e.__class__.__name__}: {e}')

