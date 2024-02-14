import requests
def get_weather(city):
    api_key = 'fb76793297cd535cabbcbc4063150457'  # Replace with your own API key
    base_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        weather_data = {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }
        return weather_data
    else:
        return None
def main():
    city = input("Enter city name: ")
    weather = get_weather(city)
    if weather:
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
        print(f"Description: {weather['description']}")
    else:
        print("Failed to retrieve weather data.")
if __name__ == "__main__":
    main()
