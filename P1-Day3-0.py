import requests

api_key = '34312fadf5cfb7dd82989c30a6055658'
city = 'London'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

print("URL:", url)

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    print(f"Weather in {city}:")
    print(f"Description: {weather_description}")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print(f"Failed to get weather data, status code: {response.status_code}")


