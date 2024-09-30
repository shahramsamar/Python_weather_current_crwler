import json
import requests
import csv
import os.path


DEBUG = True

url ="https://api.open-meteo.com/v1/forecast"

params = {
    "latitude":52.52,
    "longitude":13.41,
    "hourly":"relative_humidity_2m,wind_speed_180m,temperature_180m,soil_temperature_54cm"
}


# response = requests.get(url, params=params)
# print(response.json())

if DEBUG:
    data = None
    with open("response_example.json") as f:
         data = f.read()
    data = json.loads(data)
    
else:
    response = requests.get(url, params=params) 
    data = response.json()
# Print the raw data to check for issues
# print("Raw data from file:", data)

# Parse the JSON data
# try:
#     data = json.loads(data)
#     print("Parsed JSON data:", data)
# except json.JSONDecodeError as e:
#     print(f"Error parsing JSON: {e}")
    
# tile, timezone, temperature, humidity, soil_temperature,wind_speed    
#                 temperature_180m, relative_humidity_2m, soil_temperature_54cm, wind_speed_180m


# function to write date to csv file
def write_to_csv(filename, data):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)

# define the filename
filename = "weather_data.csv"


# check if file exists, if not ,write the header
if not os.path.isfile(filename):
    header = ["latitude","longitude","time", "relative_humidity_2m", "wind_speed_180m", "temperature_180m","soil_temperature_54cm"]
    write_to_csv(filename, header)
    

for i in range(len(data["hourly"]["time"])):
    row = [
        data["latitude"],
        data["longitude"],
        data["hourly"]["time"][i],
        data["hourly"]["relative_humidity_2m"][i],
        data["hourly"]["wind_speed_180m"][i],
        data["hourly"]["temperature_180m"][i],
        data["hourly"]["soil_temperature_54cm"][i]
    ]
    write_to_csv(filename, row)        