import json
import requests


url ="https://api.open-meteo.com/v1/forecast"

params = {
    "latitude":52.52,
    "longitude":13.41,
    "hourly":"relative_humidity_2m,wind_speed_180m,temperature_180m,soil_temperature_54cm"
}


# response = requests.get(url, params=params)
# print(response.json())

data = None
with open('response_example.json') as f:
   data = f.read()
# data = json.loads(data)

# print(data)

# Print the raw data to check for issues
# print("Raw data from file:", data)

# Parse the JSON data
try:
    data = json.loads(data)
    print("Parsed JSON data:", data)
except json.JSONDecodeError as e:
    print(f"Error parsing JSON: {e}")