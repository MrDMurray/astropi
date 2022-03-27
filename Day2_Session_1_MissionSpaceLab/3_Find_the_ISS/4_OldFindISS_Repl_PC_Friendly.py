# This version works fine on any PC or online using Repl and Thonny 
# In 2021 ephem was changed to Skyfield for the Astro Pi. I can't get that to work on a PC, only the Pi.
# That's why I'm including this verion that is more PC friendly.
# On Thonny to run this, install ephem under Tools>Manage Packages
# Repl will install ephem automatically the first time it's run

from ephem import readtle, degree

# Latest TLE data for ISS location
name = "ISS (ZARYA)"
line1 = "1 25544U 98067A   22086.54746528  .00007553  00000+0  14224-3 0  9994"
line2 = "2 25544  51.6447  20.9354 0003979 317.3996  16.1142 15.49578066332518"
iss = readtle(name, line1, line2)

def get_latlon():
    iss.compute() # Get the lat/long values from ephem
    return (iss.sublat / degree, iss.sublong / degree)

latitude, longitude = get_latlon()

print("ISS is currently at ",latitude,longitude)