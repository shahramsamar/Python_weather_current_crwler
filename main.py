import requests

url ="https://api.open-meteo.com/v1/forecast"

params = {
    "latitude":52.52,
    "longitude":13.41,
    "hourly":"relative_humidity_2m,wind_speed_180m,temperature_180m,soil_temperature_54cm"
}


response = requests.get(url, params=params)
print(response.json())