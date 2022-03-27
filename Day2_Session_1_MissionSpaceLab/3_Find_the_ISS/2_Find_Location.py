from orbit import ISS
location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
print(location)

print(f'Latitude: {location.latitude}')
print(f'Longitude: {location.longitude}')
print(f'Elevation: {location.elevation.km}')

print(f'Lat: {location.latitude.degrees:.1f}, Long: {location.longitude.degrees:.1f}')