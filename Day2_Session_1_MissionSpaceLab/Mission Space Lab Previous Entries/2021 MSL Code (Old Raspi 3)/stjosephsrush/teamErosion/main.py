# this is team erosion code
# We live by the sea so we're interested in looking at coastline erosion

from logzero import logger, logfile
from ephem import readtle, degree
from picamera import PiCamera
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
import csv



# Find that ISS
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"

iss = readtle(name, line1, line2)



dir_path = Path(__file__).parent.resolve()

# Captains log
logfile(dir_path / "Teamerosion.log")

# Set up camera
photomachine = PiCamera()
photomachine.resolution = (2592, 1944)


def aWildCSVAppears(data_file):
    """create CSV"""
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Photo", "Lat", "Long")
        writer.writerow(header)

def mOARCsvDataPlz(data_file, data):
    """add data into new row in csv"""
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)



def get_laon():
    """turn lattitude and longitude in degrees."""
    iss.compute()  # Get the lat/long values from ephem
    return (iss.sublat / degree, iss.sublong / degree)


def capture(camera, image):
    """Use `camera` to take pictures."""
    iss.compute()  # Get values from ephem
    # take the images
    camera.capture(image)


print("A long time ago...")
sleep(1)
print("In an ISS far far at least 408km away")
sleep(2)


print("")
print(".___________. _______     ___      .___  ___.               ")            
print("|           ||   ____|   /   \     |   \/   |                  ")         
print("`---|  |----`|  |__     /  ^  \    |  \  /  |                    ")       
print("    |  |     |   __|   /  /_\  \   |  |\/|  |                        ")   
print("    |  |     |  |____ /  _____  \  |  |  |  |                          ") 
print("    |__|     |_______/__/     \__\ |__|  |__|                           ")
print("                                                                        ")
print(" _______ .______        ______        _______. __    ______   .__   __. ")
print("|   ____||   _  \      /  __  \      /       ||  |  /  __  \  |  \ |  | ")
print("|  |__   |  |_)  |    |  |  |  |    |   (----`|  | |  |  |  | |   \|  | ")
print("|   __|  |      /     |  |  |  |     \   \    |  | |  |  |  | |  . `  | ")
print("|  |____ |  |\  \----.|  `--'  | .----)   |   |  | |  `--'  | |  |\   | ")
print("|_______|| _| `._____| \______/  |_______/    |__|  \______/  |__| \__| ")
print("                                                                        ")
sleep(1)


print("Now collecting data")

# start the CSV file
data_file = dir_path / "team_Erosion_Data.csv"
aWildCSVAppears(data_file)
# start the photo counter
photo_counter = 1
# record the start and current time
start_time = datetime.now()
now_time = datetime.now()

# run a loop for less than 180 minutes
while (now_time < start_time + timedelta(minutes=178)):
    
    
    # "do or do not, there is no try" - Master yoda (never used python)
    try:

        # get latitude and longitude
        latitude, longitude = get_laon()
        # Save the data to the file
        data = (datetime.now(), photo_counter, latitude, longitude)
        mOARCsvDataPlz(data_file, data)
        # get image
        image_file = f"{dir_path}/photo_{photo_counter:03d}.jpg"
        capture(photomachine, image_file)
        
        logger.info(f" Stay on target! We're on point {photo_counter}")
        photo_counter += 1
        sleep(15)
        # update the current time
        now_time = datetime.now()
        
    # "Apology excepted Catpain Needa" - Darth Vader (accepted but ...whatver)
    except Exception as e:
       logger.error('{}: {})'.format(e.__class__.__name__, e))
       
print("The loop has finished")
print("The circle is now complete")

