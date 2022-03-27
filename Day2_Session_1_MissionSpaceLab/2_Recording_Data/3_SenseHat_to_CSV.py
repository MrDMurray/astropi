import csv
from sense_hat import SenseHat
from datetime import datetime
from pathlib import Path
from time import sleep

sense = SenseHat()

base_folder = Path(__file__).parent.resolve()
data_file = base_folder'data.csv'

with open(data_file, 'w', buffering=1) as f
    writer = csv.writer(f)
    header = (Datetime, Temperature, Humidity)
    writer.writerow(header)
    for i in range(10)
        row = (datetime.now(), sense.temperature, sense.humidity)
        writer.writerow(row)
        sleep(60)