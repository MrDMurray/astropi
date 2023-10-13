import math

# Constants
earth_radius = 6371000  # in meters
iss_altitude = 408000  # in meters
orbit_time = 92 * 60  # in seconds, 92 minutes converted to seconds

# Calculate the circumference of the ISS orbit
orbit_circumference = 2 * math.pi * (earth_radius + iss_altitude)

# Calculate the speed of the ISS
iss_speed = orbit_circumference / orbit_time

print("The speed of the ISS is approximately", round(iss_speed, 2), "meters per second.")
