
# This is the Magneto Code

# We are Colin, Nicki and Josh

# We're measuring the magnetosphere around the earth!
from ephem import readtle, degree
from logzero import logger, logfile
from sense_hat import SenseHat


from datetime import datetime, timedelta
from time import sleep
from pathlib import Path
import csv

print("Magneto Program started")


####### CODE FOR SENSE HAT LOGO

# sets up sense hat
sh = SenseHat()


green = (0, 255, 0)
red = (255, 0, 0)
nothing = (0, 0, 0)
b = (0, 255, 0)
w = (255, 255, 255)

#make some colours
G = green
R = red
O = nothing

def magnetoLogo():
    
    magLogo = [
    G, O, O, O, O, O, O, G, 
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, O, R, O, 
    O, R, O, R, R, R, R, O,
    O, R, O, O, R, O, R, O,
    O, R, O, O, O, O, R, O,
    O, R, O, O, O, O, R, O,
    G, R, O, O, O, O, R, G,
    ]
    return magLogo


def magnetoLogo2():

    magLogo = [
    O, O, O, O, O, O, O, O, 
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, O, R, O, 
    O, R, G, R, R, R, R, O,
    O, R, G, G, R, G, R, O,
    O, R, G, G, G, G, R, O,
    O, R, G, O, O, G, R, O,
    O, R, G, O, O, G, R, O,
    ]
    return magLogo

# play intro logo

images = [magnetoLogo, magnetoLogo2]

for x in range(6): 
    sh.set_pixels(images[x % len(images)]())
    sleep(1)


# MAIN DATA COLLECTION CODE STARTS HERE


dir_path = Path(__file__).parent.resolve()

# magnetos log
logfile(dir_path / "magneto.log")

# Latest TLE data for ISS location
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   21050.35666428  .00001943  00000-0  43448-4 0  9992"
line2 = "2 25544  51.6441 205.5251 0003032  33.1814  49.2099 15.48980511270331"
iss = readtle(name, line1, line2)


def magnetoLogo():
    G = green
    R = red
    O = nothing
    magLogo = [
    G, O, O, O, O, O, O, G, 
    O, R, O, O, O, O, R, O,
    O, R, R, O, O, O, R, O, 
    O, R, O, R, R, R, R, O,
    O, R, O, O, R, O, R, O,
    O, R, O, O, O, O, R, O,
    O, R, O, O, O, O, R, O,
    G, O, O, O, O, O, R, G,
    ]
    return magLogo



def coffeeLoadingProgramWorking():
        
    # new colour pallette

    g = (0, 255, 0)
    r = (255, 0, 0)
    w = (255,255,255)
    n = (0,0,0)



    picture1 = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]



    picture2 = [
        g, g, g, g, g, g, g, g,
        g, g, n, g, g, n, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]



    picture3 = [
        g, g, n, g, g, n, g, g,
        g, g, g, n, g, n, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]




    picture4 = [
        g, n, g, g, n, g, g, g,
        g, g, n, g, g, n, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]


    picture5 = [
        g, n, g, g, n, g, g, g,
        g, g, g, g, g, g, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]


    picture6 = [
        n, g, g, n, g, g, g, g,
        g, g, g, g, g, g, g, g,
        r, r, r, r, r, r, r, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, w, r,
        r, w, r, r, r, r, r, r,
        r, r, w, r, r, r, r, g,
        g, r, r, r, r, r, g, g
    ]

      
    coffeeLoading = [picture1, picture2, picture3, picture4, picture5, picture6]

    for x in range(3):
        sh.set_pixels(picture1)
        sleep(0.2)
        sh.set_pixels(picture2)
        sleep(0.2)
        sh.set_pixels(picture3)
        sleep(0.2)
        sh.set_pixels(picture4)
        sleep(0.2)
        sh.set_pixels(picture5)
        sleep(0.2)
        sh.set_pixels(picture6)




def latandlonfound():
    # Gets the lat and log to put with our measurements
    iss.compute()  # finds the latitude and longitude
    return (iss.sublat / degree, iss.sublong / degree)


def newcsvcreated(data_file):
    # this function makes a csv file
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "DataPoint", "MagneticRawXYZ", "Lat","Long")
        writer.writerow(header)


def csvadded(data_file, data):
    # this function adds the data each time
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)




# starts csv file
data_file = dir_path / "magnetoData.csv"
newcsvcreated(data_file)

# starts counting dataPoints
dataPointCounter = 1


# record the two times

start_time = datetime.now()
now_time = datetime.now()

# show logo
magnetoLogo()


# loops for three hours
while (now_time < start_time + timedelta(minutes=178)):
    
    
    try:
        
        # first record the magnetic field
        

        rawMagnetometer = sh.get_compass_raw()
        #print("x: {x}, y: {y}, z: {z}".format(**raw))
    
        
        
        # then find latitude and longitude
        latitude, longitude = latandlonfound()
        
        
        # Get the data ready to go into the file
        data = (datetime.now(), dataPointCounter, rawMagnetometer, latitude,
                longitude)
        
        # use the function to place them into the csv file
        csvadded(data_file, data)
        

        logger.info(f"iterations counted so far: {dataPointCounter}")
        
        dataPointCounter += 1
        
        sleep(3)
        
        
        # updates the time
        
        now_time = datetime.now()
        
        sh.show_message(str(dataPointCounter))
        coffeeLoadingProgramWorking()
        
        
        
    except Exception as e:
        logger.error('{}: {})'.format(e.__class__.__name__, e))



# LAST PART OF PROGRAM
# This bit is just for fun!


# for some reason the sense_hat reads 0 on the first pressure reading (maybe a cold start?)
# So here we run it 3 times to wake it up and use the last value



pressure = sh.get_pressure()
sleep(2)
pressure = sh.get_pressure()
sleep(2)
pressure = sh.get_pressure()


print("Pressure: is ", round(pressure,2) , "Millibars")

# checks if pressure in ISS is less than 300hPa
if pressure < 300: 


  sh.show_message("DON'T PANIC")

  print(" ")
  print(" ")
  print("  _____   ____  _   _ _ _______   _____        _   _ _____ _____   ")
  print("|  __ \ / __ \| \ | ( )__   __| |  __ \ /\   | \ | |_   _/ ____|   ")
  print(" | |  | | |  | |  \| |/   | |    | |__) /  \  |  \| | | || |       ")
  print(" | |  | | |  | | . ` |    | |    |  ___/ /\ \ | . ` | | || |       ")
  print(" | |__| | |__| | |\  |    | |    | |  / ____ \| |\  |_| || |____   ")
  print(" |_____/ \____/|_| \_|    |_|    |_| /_/    \_\_| \_|_____\_____|  ")
  print("                                                                   ")
                                                                 
  print("Space is 99.99% vacuum. If anything, THIS is far more normal by the standards of the universe.")
  
else:
    print("All is good. Program complete. Thanks")
    
magnetoLogo()
 

w = (255, 255, 255)

r = (255, 0, 0)
g = (0, 255, 0)
b = (0, 0, 255)

n = (255, 0, 0)


finishedPic = [
    r, r, w, r, w, r, r, r,
    r, w, w, w, w, r, w, r,
    r, r, w, r, w, r, w, r,
    r, w, w, r, w, r, w, r,
    r, w, w, r, w, r, w, r,
    g, b, b, g, b, g, b, g,
    g, b, b, g, b, g, b, g,
    g, b, b, g, b, g, b, g
]

sh.set_pixels(finishedPic)
    
    


