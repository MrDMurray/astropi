import csv
from sense_hat import SenseHat
from datetime import datetime
from pathlib import Path
from time import sleep

def create_csv(data_file):
    with open(data_file, 'w') as f:
        writer = csv.writer(f)
        header = ("Date/time", "Temperature", "Humidity")
        writer.writerow(header)

def add_csv_data(data_file, data):
    with open(data_file, 'a') as f:
        writer = csv.writer(f)
        writer.writerow(data)

sense = SenseHat()

base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'

create_csv(data_file)
for i in range(10):
    row = (datetime.now(), sense.temperature, sense.humidity)
    add_csv_data(data_file, row)
    sleep(60)