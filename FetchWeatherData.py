import json
def fetch_weather_from_json(file_path):
with open(file_path, 'r') as f:
data = json.load(f)
location = data['location']['name']
country = data['location']['country']
temperature = data['current']['temperature']
humidity = data['current']['humidity']
wind_speed = data['current']['wind_speed']
description = data['current']['weather_descriptions'][0]
print(f"Weather Report for {location}, {country}")
print(f"Condition : {description}")
print(f"Temperature : {temperature}°C")
print(f"Humidity : {humidity}%")
print(f"Wind Speed : {wind_speed} km/h")
# Example usage
fetch_weather_from_json("weather.json")

 OUTPUT
Weather Report for Chennai, India
Condition : Partly cloudy
Temperature : 31°C
Humidity : 76%
Wind Speed : 12 km/h
