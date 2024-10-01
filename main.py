import json
import requests
import csv
import os.path


# define the filename
output_filename = "weather_data.csv"
latitude_longitude_list = []

with open("geo_location.csv", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        latitude_longitude_list.append((float(row['latitude']),float(row['longitude'])))



def get_forecast_data(lat, lon):
    url ="https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude":lat,
        "longitude":lon,
        "hourly":"relative_humidity_2m,wind_speed_180m,temperature_180m,soil_temperature_54cm"
    }
    response = requests.get(url, params=params)
    return response.json()

   
# function to write date to csv file
def write_to_csv(filename, data):
    with open(filename, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(data)
# check if file exists, if not ,write the header
if not os.path.isfile(output_filename):
    header = ["latitude","longitude","time", "relative_humidity_2m", "wind_speed_180m", "temperature_180m","soil_temperature_54cm"]
    write_to_csv(output_filename, header)
    


# loop over latit
for lat,lon in latitude_longitude_list:
    data = get_forecast_data(lat,lon)
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
        write_to_csv(output_filename, row)        