import requests

api_key = 'e46b4e6dd0cf9374db7cbd7c90dc35d8'

user_input = input("Enter city: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])
country = weather_data.json()['sys']['country']

print(f"Location: {user_input},{country}")
print(f"Weather: {weather}")
print(f"Temperature: {temp}ºC")

