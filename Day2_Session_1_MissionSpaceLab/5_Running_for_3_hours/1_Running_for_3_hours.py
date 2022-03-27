from datetime import datetime, timedelta
from time import sleep

# Create a `datetime` variable to store the start time
start_time = datetime.now()
# Create a `datetime` variable to store the current time
# (these will be almost the same at the start)
now_time = datetime.now()
# Run a loop for 2 minutes
while (now_time < start_time + timedelta(minutes=2)):
    print("Doing stuff")
    sleep(1)
    # Update the current time
    now_time = datetime.now()