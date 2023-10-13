## Method 1: Getting Speed Using Distance and Time

### Calculating the Speed of the ISS Using Speed-Distance-Time Formula

#### Introduction

The speed of an object in constant motion can be calculated using the simple formula:

\`\`\`
Speed = Distance / Time
\`\`\`

We can use this formula to calculate the speed of the International Space Station (ISS) as it orbits Earth.

#### The Math Behind It

1. **Orbit Circumference**: The ISS orbits Earth at an altitude of about 408,000 meters. The Earth's radius is approximately 6,371,000 meters. To find the distance the ISS travels in one complete orbit, we calculate the circumference of the circle defined by its orbit:

\`\`\`
Circumference = 2 * pi * (Earth's Radius + ISS Altitude)
\`\`\`

2. **Time for One Orbit**: The ISS takes about 92 minutes to complete one orbit. To convert this time into seconds (for consistency with our distance unit, meters), we use:

\`\`\`
Time in seconds = 92 * 60
\`\`\`

3. **Speed of ISS**: With the Distance (Circumference) and Time known, we can now find the speed using the formula:

\`\`\`
Speed = Circumference / Time in seconds
\`\`\`

#### Python Code

\`\`\`python
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
\`\`\`

---

## Method 2: Gravitational Force

The gravitational force between two masses is given by the formula:

\`\`\`
F = (G * m1 * m2) / r^2
\`\`\`

Here, `F` is the gravitational force, `G` is the gravitational constant, `m1` and `m2` are the masses, and `r` is the distance between them.

The centripetal force `F` that keeps the ISS in orbit is equal to `m * a`, where `m` is the mass of the ISS and `a` is the centripetal acceleration, `v^2 / r`.

Equating the two forces and solving for velocity `v`, we get:

\`\`\`
v = sqrt(G * M / r)
\`\`\`

Where:
- `G` is the gravitational constant `6.67430 x 10^-11 m^3/kg s^2`
- `M` is the mass of Earth `5.972 x 10^24 kg`
- `r` is the distance from the center of Earth to the ISS

---
