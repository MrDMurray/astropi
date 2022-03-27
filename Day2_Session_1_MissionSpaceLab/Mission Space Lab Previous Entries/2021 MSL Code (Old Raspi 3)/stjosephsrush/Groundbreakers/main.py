# ground-breakers code
# Our target is both sea and land areas


from logzero import logger, logfile
from ephem import readtle, degree
from picamera import PiCamera
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
import csv

# We'd also like to measure Temperature and Humidity in the ISS just because why not
from sense_hat import SenseHat

# sets up sense hat
sh = SenseHat()

# bassically a find my spacestation app 
# updated this code on 19/02/21

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"
spaceyMacStationGuy = readtle(name, line1, line2)



# the title of my log and the path for stuff :)
dir_path = Path(__file__).parent.resolve()
logfile(dir_path/"groundbreakers.log")




# getting the perfect camera angles
pictionary = PiCamera()
pictionary.resolution = (2592, 1944)

def producerofCSV(doc_ment):
    """Produces a Fine CSV of the Highest Quality"""
    with open(doc_ment, 'w') as f:
        writer = csv.writer(f)
        header = ("DataTime","DataPoint","Humidity","Temperature","latitude","longitude","Acceleration","CompassRaw", "Compass")
        writer.writerow(header)

def gimmemoreDATA (data_file, data):
    """Add a nice new row of data to the CSV"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

def getthatLATLON():
    """send back the current latitude and longitude, in degrees"""
    spaceyMacStationGuy.compute() # Get the lat/long values from ephem
    return (spaceyMacStationGuy.sublat / degree, spaceyMacStationGuy.sublong / degree)


def capture(camera, image):
    """Use `camera` to capture an `image` file with lat/long & time  data."""
    spaceyMacStationGuy.compute() # Get the lat/long values from ephem
    # capture the image
    camera.capture(image)


# initialise the CSV file
data_file = dir_path/"groundBreakers_data.csv"
producerofCSV(data_file)


# start the photo and data counter
dataCounter = 1

# record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# run the main loop
while (now_time < start_time + timedelta(minutes=170)):
    try:
        
        #get A BUNCH of sensor data
        
        humidity = round(sh.humidity, 4)
        temperature = round(sh.temperature, 4)
        pressure = round(sh.pressure, 4)

        sleep(1)
        compass = (sh.compass)
        compassRAW = (sh.compass_raw)
        acceleration = (sh.accelerometer_raw)
        
        # get latitude and longitude
        latitude, longitude = getthatLATLON()
        # Save the data to the file
        data = (
            datetime.now(),dataCounter,humidity,temperature,latitude,longitude,acceleration,compass, compassRAW
        )
        
        gimmemoreDATA(data_file, data)
        # capture image
        image_file = f"{dir_path}/photo_{dataCounter:03d}.jpg"
        capture(pictionary, image_file)
        logger.info(f"iteration {dataCounter}")
        dataCounter += 1
        sleep(15)
        # update the current time
        now_time = datetime.now()
        
        
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))
        
print("All done") 

