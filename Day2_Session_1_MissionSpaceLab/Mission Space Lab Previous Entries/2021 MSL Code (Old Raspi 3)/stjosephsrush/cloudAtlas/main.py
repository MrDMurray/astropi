# Cloud Atlas -- Daniel and Jordan
# For measuring cloud Albedo
# Target: Clouds!


# prints logo

print("")
print("")
print("         .-~~~-. ")
print("  .- ~ ~-(       )_ _   ")
print(" /                     ~ -.   ")
print("|     CLOUD ATLAS          \  ")
print(" \                         .'   ")
print("  ~- . _____________ . -~   ")
print("")
print("I believe there is another world waiting for us. ")



from logzero import logger, logfile
from ephem import readtle, degree
from picamera import PiCamera
from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
import csv

dir_path = Path(__file__).parent.resolve()

# Sets a name for our 'Cloud Atlas'
logfile(dir_path/"cloud-atlas.log")

# I am here!
name = "ISS (ZARYA)"

# ephem data from NORAD 19/02/21

name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"

iss = readtle(name, line1, line2)

# Mum, get the camera 
photocapture= PiCamera()
photocapture.resolution = (2592, 1944)


def get_latlon():
    """Return our location, through Latiude-Longitude format, in Degrees"""
    iss.compute() # Get the lat/long values from ephem
    return (iss.sublat / degree, iss.sublong / degree)



# CSVS

def filecreate(space_scrolls):
    """Create a new datasheet for the details,  and add the first part, the header row"""
    with open(space_scrolls, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Picture", "Lat", "Long")
        writer.writerow(header)

def add_csv_data(space_scrolls, data):
    """Add a row of data to the data_file CSV"""
    with open(space_scrolls, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)
        



def convert(angle):
    """
    Converts an angle. with complex telemtry data and mathematics! 
    """
    degrees, minutes, seconds = (float(field) for field in str(angle).split(":"))
    exif_angle = f'{abs(degrees):.0f}/1,{minutes:.0f}/1,{seconds*10:.0f}/10'
    return degrees < 0, exif_angle

def capture(camera, image):
    """Use our camera to snap a picture of the Earth, with our location included"""
    iss.compute() # Get the lat/long values from ephem

    # convert the latitude and longitude to EXIF-appropriate representations
    south, exif_latitude = convert(iss.sublat)
    west, exif_longitude = convert(iss.sublong)

    # set the EXIF tags specifying the current location
    camera.exif_tags['GPS.GPSLatitude'] = exif_latitude
    camera.exif_tags['GPS.GPSLatitudeRef'] = "S" if south else "N"
    camera.exif_tags['GPS.GPSLongitude'] = exif_longitude
    camera.exif_tags['GPS.GPSLongitudeRef'] = "W" if west else "E"

    # capture the image
    camera.capture(image)



# initialise the photo counter
photo_counter = 1


# initialise the CSV file
space_scrolls = dir_path/"cloudAtlasData.csv"
filecreate(space_scrolls)

# record the start and current time
start_time = datetime.now()
now_time = datetime.now()


# run for three hours
while (now_time < start_time + timedelta(minutes=176)):
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
        add_csv_data(space_scrolls, data)
        
        # print("Taking a photo now")
        
        
        
        # capture image
        our_pic = f"{dir_path}/photo_{photo_counter:03d}.jpg"
        capture(photocapture, our_pic)
        logger.info(f"iteration {photo_counter}")
        photo_counter += 1
        
        
        # reports to the iss crew that program is working (every 5th go)
        if photo_counter % 5 == 0:
            print("It's working! Keep going little program")
               
        sleep(15)
        # update the current time, right now!!
        now_time = datetime.now()
        
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))
        
print("Finished!")

print("Daniel's Message to the crew: I'm sending a huge wave to you folks up there at the moment! Back here on earth we find ourselves ina somewhat more comparable situation - our everyday world and space seems to have shrunk and has become a little more confined, being at home a lot more than usual, and having to come up with new ideas and inventions to keep everyday life on the straight and flat. Its always been factthat of course the ISS is a place where you live with obvious limitations of where you can go and confinement is clear, but at the moment it does seem that there is a degree of freedom and 'out there' nature when I think of you astronauts hundreds of kilometres above from where I am standing!")

