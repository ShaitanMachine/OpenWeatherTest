import requests

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY"
    response = requests.get(url)
    data = response.json()
    temperature = data["main"]["temp"]
    weather_description = data["weather"][0]["description"]
    return temperature, weather_description

def main():
    city = input("Enter a city name: ")
    temperature, weather_description = get_weather(city)
    print(f"The current temperature in {city} is {temperature}°C.")
    print(f"The weather is {weather_description}.")
