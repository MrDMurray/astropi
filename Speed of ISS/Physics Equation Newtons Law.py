
import math

# Constants
G = 6.67430e-11  # Gravitational constant in m^3/kg s^2
M = 5.972e24  # Mass of Earth in kg
earth_radius = 6371000  # Radius of Earth in meters
iss_altitude = 408000  # Altitude of ISS in meters

# Calculate distance from center of Earth to ISS
r = earth_radius + iss_altitude

# Calculate the speed of ISS using Newton's Law of Gravitation
iss_speed = math.sqrt((G * M) / r)

print("The speed of the ISS is approximately", round(iss_speed, 2), "meters per second.")
